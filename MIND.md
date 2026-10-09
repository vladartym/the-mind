# How the mind works

This folder is an LLM wiki, after the
[idea file by Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
The user gives sources. The agent reads them and writes linked pages. The pages
compound: each new source adds to the pages that already exist.

## The one rule

**Sort by who the knowledge is about, not by how it arrived.**

A reader asks who a page is about, not which pipeline made it. So the folders
say who a thing is about.

## The layers

- **Raw sources** — `raw/`. Each source as it arrived. Nothing in it is edited
  or deleted.
  - `raw/videos/<slug>/` — YouTube audio, transcript and metadata.
  - `raw/articles/<slug>/` — web articles as markdown.
  - `raw/files/<slug>/` — local files, such as PDFs, and anything with no
    other folder.
  - `raw/transcripts/<slug>/` — recordings: the audio, the transcript and
    metadata.
  - `raw/photos/<slug>/` — pictures, with the caption that came with them.
  - `raw/notes/` — short notes, one file each, under the name they arrived
    with.

  A page is one reading of a source. A reader who doubts the reading needs the
  source to check it against. That is why the source stays.

- **Pages** — `pages/`. Markdown that the agent writes and keeps. The user
  reads it. All pages are in one link space, so any page can link to any other
  page. There are three areas:

  - `pages/world/` — **other people's work.** One page for each ingested
    source, and a page for each concept, tool, app, company and person that the
    sources name. Nobody in `pages/world/people/` knows the user.
  - `pages/self/` — **the user.** The people the user sees, the home, the
    plans. `pages/self/people/` is the opposite of `pages/world/people/`: these
    are people the user knows, and their work is not the subject.
  - `pages/work/` — **what the user builds or is paid for.** One folder for
    each client or product, each with an `index.md`.

- **Data** — `data/`. Ledgers, not prose. Each folder has a `README.md` with its
  schema. `data/todo/` is the task list. Add a folder when you have a new
  ledger, such as money or trips.

- **The schema** — `CLAUDE.md` and this file. The rules and the conventions.

- **The inbox** — `dropbox/`. Put any file here and say `/dropbox`. The agent
  copies each file into `raw/` first, and then files it. Git ignores this
  folder, so a file that leaves it without a copy in `raw/` is lost.

## Special files

- `pages/index.md` — the front page. It names the three areas. Read it when you
  do not know where a thing goes.
- `pages/world/index.md`, `pages/self/index.md`, `pages/work/index.md` — the
  catalog of each area, with a one-line summary for each page.
- `pages/log.md` — a record that only grows, for all three areas. Each entry
  starts like this:
  ```
  ## [YYYY-MM-DD] ingest | <title>
  ```

## Ingest flow

1. Make the raw source. The `ingest` skill has a handler for each type.
2. Read the raw source in full.
3. Tell the user the main points, the new pages that you propose, and the
   changes to existing pages. Wait for the user to reply.
4. Write the pages: a source page, and the entity and concept pages that the
   source changes. If the source contradicts an older source, say so on the
   page.
5. Put the raw path on the source page: `**Source:** \`raw/videos/<slug>/\``.
   Other pages reach the source through their `[[link]]` to the source page.
6. Add the new pages to the index of the area. Add an entry to `pages/log.md`.

## Conventions

- **Pages link with `[[wiki-links]]`.** A link uses the file name, not the path,
  so it still works when a page moves to a different folder. A link can go from
  any area to any other area.
- Do not define page shapes, frontmatter or subfolders in advance. Let them
  come from use. When a pattern is stable, write it down here.
- Give an entity or a concept its own page when it will probably come back, or
  when it connects pages that exist.
- A channel, a podcast or a publication is an entity page under
  `pages/world/channels/`. It is not a folder above the other pages.
- **A page is about one subject.** When a person, a company or a client shows
  up in three places, write the page that those three places link to.

## Query

When the user asks a question, read the index of the area that the question is
about. Then read the pages it points to, and answer with links to them.

If the answer is a useful synthesis, such as a comparison or a new connection,
save it as a new page. Do not let good answers stay only in the chat.

## Lint

When the user asks for a lint, look for:

- Contradictions between pages.
- Claims that a newer source replaced.
- Orphan pages, which no page links to.
- Concepts that pages mention but that have no page.
- Missing links in the other direction.
- Duplicate pages about one subject under two names.
- Two different people with the same first name and no note to tell them apart.
- A subject named in three places with no page of its own.

The `lint` skill has the full steps.
