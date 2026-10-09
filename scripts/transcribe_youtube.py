#!/usr/bin/env python3
"""Download a YouTube video's audio and transcribe it with faster-whisper."""

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

import yt_dlp

DEFAULT_MODEL = "large-v3"

# mlx-whisper (Apple MLX, GPU-accelerated) is ~10x faster than faster-whisper on
# CPU int8, which is what makes large-v3 viable as the default. Falls back to
# faster-whisper when mlx is unavailable (non-Apple-Silicon, or not installed).
MLX_REPOS = {
    "tiny": "mlx-community/whisper-tiny-mlx",
    "base": "mlx-community/whisper-base-mlx",
    "small": "mlx-community/whisper-small-mlx",
    "medium": "mlx-community/whisper-medium-mlx",
    "large-v3": "mlx-community/whisper-large-v3-mlx",
    "large-v3-turbo": "mlx-community/whisper-large-v3-turbo",
}


def slugify(text: str, max_len: int = 80) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:max_len].strip("-").lower() or "untitled"



# YouTube blocks plain requests: it needs a signed-in cookie jar and a JavaScript
# runtime to solve the player challenge. Chrome cookies plus the ejs solver are
# what get a 403 down to a working download.
ANTI_BOT_OPTS = {
    "cookiesfrombrowser": ("chrome", None, None, None),
    "remote_components": ["ejs:github"],
}

def fetch_info(url: str) -> dict:
    with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True, **ANTI_BOT_OPTS}) as ydl:
        return ydl.extract_info(url, download=False)


def download_audio(url: str, video_dir: Path) -> Path:
    opts = {
        "format": "bestaudio/best",
        "outtmpl": str(video_dir / "audio.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        **ANTI_BOT_OPTS,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    return video_dir / "audio.mp3"


def transcribe_mlx(audio_path: Path, model_size: str) -> tuple[str, str]:
    import mlx_whisper

    repo = MLX_REPOS.get(model_size)
    if repo is None:
        raise ValueError(f"no mlx repo mapped for model {model_size!r}")
    # condition_on_previous_text feeds each window the last one's text. On a
    # pause or a music bed the model then repeats the last line for minutes and
    # eats the speech underneath it. Whole answers were lost this way. Off, the
    # windows are independent, which costs a little context and loses nothing.
    result = mlx_whisper.transcribe(
        str(audio_path), path_or_hf_repo=repo, condition_on_previous_text=False
    )
    return result.get("language", "unknown"), result["text"].strip()


def transcribe_faster_whisper(audio_path: Path, model_size: str) -> tuple[str, str]:
    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(audio_path), beam_size=5)
    transcript = " ".join(seg.text.strip() for seg in segments)
    return info.language, transcript


def transcribe(audio_path: Path, model_size: str, runner: str) -> tuple[str, str, str]:
    """Returns (language, transcript, runner_actually_used)."""
    if runner in ("auto", "mlx"):
        try:
            return (*transcribe_mlx(audio_path, model_size), "mlx-whisper")
        except Exception as exc:
            if runner == "mlx":
                raise
            print(f"mlx-whisper unavailable ({exc}); falling back to faster-whisper.")
    return (*transcribe_faster_whisper(audio_path, model_size), "faster-whisper")


def format_duration(seconds: int | None) -> str:
    if not seconds:
        return "unknown"
    return str(timedelta(seconds=int(seconds)))


def format_upload_date(raw: str | None) -> str:
    if not raw:
        return "unknown"
    try:
        return datetime.strptime(raw, "%Y%m%d").strftime("%Y-%m-%d")
    except ValueError:
        return raw


def write_metadata(path: Path, info: dict, language: str, model: str, runner: str) -> None:
    lines = [
        f"# {info['title']}",
        "",
        f"- **Channel:** {info.get('uploader', 'unknown')}",
        f"- **URL:** https://www.youtube.com/watch?v={info['id']}",
        f"- **Video ID:** {info['id']}",
        f"- **Duration:** {format_duration(info.get('duration'))}",
        f"- **Uploaded:** {format_upload_date(info.get('upload_date'))}",
        f"- **Language:** {language}",
        f"- **Model:** {model}",
        f"- **Runner:** {runner}",
        "",
    ]
    path.write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help="Whisper model size: tiny, base, small, medium, large-v3 "
                             f"(default: {DEFAULT_MODEL})")
    parser.add_argument("--runner", default="auto", choices=("auto", "mlx", "faster-whisper"),
                        help="auto tries mlx-whisper (GPU) then falls back to faster-whisper (CPU)")
    parser.add_argument("--videos-dir", type=Path, default=Path("raw/videos"))
    args = parser.parse_args()

    info = fetch_info(args.url)
    slug = f"{slugify(info['title'])}-{info['id']}"
    video_dir = args.videos_dir / slug
    video_dir.mkdir(parents=True, exist_ok=True)

    print(f"Title: {info['title']}")
    print(f"Folder: {video_dir}")

    audio_path = download_audio(args.url, video_dir)

    print(f"Transcribing with model={args.model} (runner={args.runner})...")
    language, transcript, runner = transcribe(audio_path, args.model, args.runner)

    (video_dir / "transcript.txt").write_text(transcript + "\n")
    write_metadata(video_dir / "metadata.md", info, language, args.model, runner)

    print(f"Done: {video_dir}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
