---
name: ingest-all
description: Batch-ingest every raw source not yet in the wiki, running subagents in parallel waves. Use when the user says "ingest all", "process the new ones", or after adding multiple raw files.
---

# ingest-all

Ingest every source in `raw/` that has no entry in `pages/log.md`.

1. **Find the new sources.** List `raw/videos/*/`, `raw/articles/*/` and
   `raw/files/*/`. Remove each slug that an ingest entry in `pages/log.md`
   already names. Show the list before you start. If there are more than 10,
   tell the user and propose a plan of waves first.
2. **Run subagents in waves of up to 8.** Start all agents of a wave in one
   message. Each agent reads `MIND.md`, `pages/world/index.md` and its own raw
   source. It writes only new pages: the source page and new entity, concept
   or tool pages. It must not edit `pages/world/index.md`, `pages/log.md`, or
   any page that already exists. It returns:
   - the paths of its new pages,
   - the edits it proposes to existing pages, as exact old and new strings,
   - a draft log entry,
   - open questions.
3. **Merge after each wave.** Apply the proposed edits one at a time, and
   combine edits that two agents made to the same page. Add the log entries.
   Update `pages/world/index.md`. Start the next wave only after this, so that
   its agents see the pages of the wave before.
4. **Report after each wave.** For each source: the pages created, the pages
   changed and the open questions. Continue until no source is left or the user
   stops you.

## Tell the user first

- **Waves are faster, but they compound less.** Agents in one wave do not see
  the pages of the others. For about 10 sources this does not matter. For 50 or
  more, each new wave recovers it.
- **For the best quality, go one at a time:** one agent for each source, and
  wait for it before the next.
