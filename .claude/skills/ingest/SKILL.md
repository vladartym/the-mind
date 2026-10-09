---
name: ingest
description: Ingest a source (YouTube URL, web article, or local file) into the wiki. Use when the user says "ingest", "add", or "process" a source.
---

# ingest

Make a raw source under `raw/`, then ingest it as `MIND.md` says.

## Handlers by source type

- **YouTube URL** (youtube.com or youtu.be):
  ```
  uv run scripts/transcribe_youtube.py <URL>
  ```
  This writes `raw/videos/<slug>/` with `audio.mp3`, `transcript.txt` and
  `metadata.md`.

  The default is Whisper `large-v3`. On Apple Silicon it runs on the GPU with
  mlx. On other machines it falls back to faster-whisper on the CPU. Do not use
  a smaller model to save time. `base` gets names wrong, and wrong names become
  wrong facts in the pages. Use `--model base` only for audio that does not
  matter.

- **Web article or URL**: get the page with WebFetch. Save it as
  `raw/articles/<slug>/article.md`, with a header that gives the title, the
  URL, the author, the date and the ingest date.

- **Local file** (PDF, markdown, text): copy it into `raw/files/<slug>/`, with
  a `metadata.md` that gives the original path, the date and the type.

If you cannot tell the source type, ask the user.

## After the raw source lands

Nothing in `raw/` is edited or deleted. Read the raw source in full. Then do
the ingest flow in `MIND.md`: tell the user the main points, write the pages,
update the index of the area, and add an entry to `pages/log.md`.

A video, an article or a file is somebody else's work, so its pages go in
`pages/world/`. Sort by who the page is about: a source about a tool that the
user now uses is still in `pages/world/`.

The source page names the folder it was written from:

```
**Source:** `raw/videos/<slug>/`
```

Entity and concept pages do not repeat it. They reach the raw source through
their `[[link]]` to the source page.
