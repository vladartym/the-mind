# Todo

Every task, one markdown file to a task. Nothing else holds the list: there is
no database, no server and no account. The `todo` skill reads and writes this
folder.

## Layout

```
data/todo/
  README.md          this file, the schema
  tags.json          the tags that a task can carry
  tasks/<slug>.md    one task
```

## One task

The file name is the identity of the task. It never changes, so a task keeps
its file when the title changes.

```markdown
---
title: file the tax return
status: open
priority: high
tags: [personal]
due: 2026-10-09
estimate: 2h
created: 2026-08-19
---

Do it before the deadline.

- [ ] find last year's return
- [x] get the slips
```

### The fields

| Field | Values | Notes |
|---|---|---|
| `title` | any text | Required. |
| `status` | `open`, `done` | Defaults to `open`. |
| `priority` | `high`, `medium`, `low`, `none` | Defaults to `none`. |
| `tags` | a list of tag names | Each name must be in `tags.json`. |
| `due` | `2026-10-09` or `2026-10-09 14:30` | Optional. |
| `estimate` | `45m`, `2h`, `1h30m` | How long the task takes. Optional. |
| `created` | `2026-08-19` | The day the task was written. |
| `done` | `2026-09-01` | The day the task was completed. |

### The body

Everything after the frontmatter is the description. A line that starts with
`- [ ]` or `- [x]` is a subtask, wherever it is in the body.

## Tags

`tags.json` is the only organisation. There are no lists and no folders. A task
carries tags, and a task with no tag is still a task. Add a tag by adding an
object to that file.

## Links

A task links to a page with `[[page-name]]`. A page links to a task with the
full path, `[[data/todo/tasks/<slug>]]`, so that a task never collides with a
page of the same name.

## Order

Sort by priority first, then by due date, soonest first. A task with no due date
comes after every task that has one.
