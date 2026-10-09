# Mind

A place to store, analyze and query knowledge. You, the agent, write and keep
the pages. The user reads them and gives you sources.

Read `MIND.md` for how it works.

## Where a thing goes

**Sort by who the knowledge is about, not by how it arrived.**

- `pages/` — markdown that you write and keep, in one link space.
  `pages/world/` is other people's work, `pages/self/` is the user,
  `pages/work/` is the user's clients and builds.
- `data/` — ledgers with a schema. `data/todo/` is the task list.
- `raw/` — sources as they arrived. Never edit or delete a file in it.
- `dropbox/` — the inbox. Git ignores it.

## Version control

Keep this folder in git. Before a bulk operation, such as a large ingest or a
lint pass, commit the current state. Commit again when the operation is done.

## More than one agent

More than one session can work in this folder at the same time.

- Stage explicit paths. Never use `git add -A` or `git add .`.
- Read `pages/log.md` and the index of the area again just before you edit
  them. Add lines to them. Do not rewrite a section.
- Make sure that a page does not already exist before you create it.
