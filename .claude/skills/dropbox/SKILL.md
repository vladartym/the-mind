---
name: dropbox
description: Sort the files in the dropbox/ inbox folder into the right place in the mind. Use when the user says "dropbox", "sort dropbox", "process the dropbox folder", or "sort the inbox". Nothing to do with Dropbox the file-sync service.
---

# dropbox

`dropbox/` is the inbox. The user puts any file in it: a note, a photo, a PDF,
a recording, a file with a list of links. For each file, copy it into `raw/`,
decide where it belongs, and write what it says into the right page.

This folder is an ingest path, the same as a YouTube link. A file in it is a
source, so it follows the rule of `raw/`: the source is kept, and it is kept
whole.

## Each file makes two moves

Do the two moves in this order:

1. **The original goes to `raw/`**, into the folder that fits it.
2. **A reading goes where it belongs**: a page, or a task. It names the raw
   path it came from.

The copy in `raw/` makes the second move safe. A page can be written again
later. A file that is lost cannot.

## Step one: where the original goes

| What arrived | Where the original goes |
| --- | --- |
| A recording: `.m4a`, `.mp3`, `.wav` | `raw/files/<slug>/`, with a `metadata.md` |
| A photograph: `.jpg`, `.png`, `.heic` | `raw/photos/<slug>/` |
| A note: `.md`, `.txt` | `raw/notes/`, under the name it arrived with |
| A link to a video or an article | Through the `ingest` skill: `raw/videos/<slug>/` or `raw/articles/<slug>/` |
| Anything else: `.pdf`, `.csv`, a file you do not know | `raw/files/<slug>/`, with a `metadata.md` that says what arrived and when |

Each file matches a row. When no other row fits, the last row fits.

`<slug>` says what the file is, with the date: `raw/photos/2026-08-11-fridge-nameplate/`.
Inside the folder, the file keeps the name it arrived with. Files that arrived
together and are about one thing go in one folder.

A recording has no transcript. Do not write a page from what you guess it
says. File it, and tell the user that it has no transcript.

## Step two: what you write from it

- **A meeting or a call:** a summary on the page of the person or the client it
  was with, such as `pages/work/<client>/meetings/<date>-<slug>.md` or
  `pages/self/people/<person>.md`. Give the date, the people, the main points,
  the decisions and the actions, and a link to the raw file.
- **A knowledge source**, such as an article or notes on a book: use the
  `ingest` skill.
- **A file for a project:** `pages/work/<project>/`.
- **A thought of the user's own:** file it by what it is about, not by the fact
  that the user wrote it. An idea about a concept goes in
  `pages/world/concepts/`. A plan for a build goes in `pages/work/<project>/`.
  Something about the user's own life goes in `pages/self/`. When the page
  exists, add to it.
- **Something to do:** add a task with the `todo` skill, and link it to the raw
  file or the page.
- **Something worth keeping that says nothing more**, such as a photo of a
  serial number: the copy in `raw/` is all the filing it needs. Say so in the
  log entry. Do not write a page that nobody will read.
- **Anything you cannot place, or that does not make sense:** the original is
  already in `raw/`, so nothing is at risk. Write no page. Ask the user.

Whatever you write names the raw path it came from.

## Ask the user

A file is often half a thought. The reason the user made it is in the user's
head, not in the file. Two cases go to the user, not to a page:

1. You cannot decide where the file belongs.
2. You can read the file, but what it says does not make sense.

Do not guess the page. A page written from a guess reads as fact to the next
agent.

Move the original into `raw/` before you ask. Never keep a file in `dropbox/`
while you wait for an answer, because git ignores `dropbox/`.

Sort each file that you can place first. Then ask about the rest in one
message. Ask a short question that names the file and says what you know:

> Three photos of a shop window, 2026-09-07, no caption. What were these for?

## When you are done

Add one entry to `pages/log.md` for each sort:

```
## [YYYY-MM-DD] sorted | <what came in>
```

Name each raw path, and each question you asked. Empty `dropbox/` only when
each file has its copy in `raw/`.
