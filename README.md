# The Mind

A second brain that an agent keeps for you. You give it sources: videos,
articles, files, notes and photos. The agent reads them and writes a wiki of
linked markdown pages. You ask questions, and good answers become new pages.

It is a folder of markdown and a set of Claude Code skills. It has no app, no
server and no database. It follows the
[LLM Wiki idea by Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Setup

1. Click **Use this template** on GitHub, or clone this repository.
2. Install `uv` and `ffmpeg`. On a Mac: `brew install uv ffmpeg`.
3. Run `uv sync`. This installs the YouTube transcriber.
4. Open the folder in Claude Code.

To read the pages, open the folder in [Obsidian](https://obsidian.md). The
`[[wiki-links]]` then work as links.

## Commands

Say these to Claude Code in the folder.

| Say | What happens |
|---|---|
| `/ingest <url or file>` | The agent saves the source in `raw/` and writes pages from it. |
| `/ingest-all` | The agent ingests every source in `raw/` that has no pages yet. |
| `/dropbox` | The agent sorts each file that you put in `dropbox/`. |
| `/query <question>` | The agent answers from the pages, and can save the answer as a page. |
| `/lint` | The agent finds duplicates, orphan pages and contradictions. |
| `/todo <task>` | The agent adds, lists or completes a task. |

## Layout

| Folder | Holds |
|---|---|
| `pages/world/` | Other people's work: sources, concepts, tools, people, companies. |
| `pages/self/` | You: the people you see, your home, your plans. |
| `pages/work/` | Your clients and the things you build. |
| `data/todo/` | Your tasks, one markdown file to a task. |
| `raw/` | Each source as it arrived. The agent never edits it. |
| `dropbox/` | An inbox. Put any file here, then say `/dropbox`. |

`MIND.md` tells how it works. `CLAUDE.md` holds the rules for the agent.
