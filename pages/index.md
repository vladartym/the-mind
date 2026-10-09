# Pages

Everything the agent writes and keeps. One link space: any page can link to
any other page with `[[wiki-links]]`. A link uses the name, not the path, so it
still works when a page moves.

Three areas, sorted by **who the knowledge is about**.

| Area | About | Start at |
|---|---|---|
| [[world]] | Other people's work. Sources, concepts, tools, apps, companies and the people behind them. Nobody in it knows the user. | `world/index.md` |
| [[self]] | The user. The people the user sees, the home, the plans. | `self/index.md` |
| [[work]] | What the user builds or is paid for. One folder for each client or product. | `work/index.md` |

The task list is not here. It is in `data/todo/`.

`log.md`, beside this file, is the record of every ingest, sort and lint pass.

## Which area does a thing go in

Ask who the page is about, not how it arrived.

- A founder on a podcast → `world/people/`.
- A friend → `self/people/`. The two folders have the same name on purpose:
  same word, opposite meaning, kept apart by the area.
- A tool that somebody else built → `world/tools/`, even if the user uses it.
- A client, a contract, a build → `work/<name>/`.
- A meeting → under the person or the client it was with.
- A pattern that is true across many sources → `world/concepts/`.
