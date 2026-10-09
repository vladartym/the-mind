---
name: todo
description: Add, list, change or complete tasks in the task list at data/todo/. Use when the user says "todo", "add a task", "remind me to", "what is on my list", "what is due", "I did X", or "mark X done".
---

# todo

Each task is one file in `data/todo/tasks/`. Read `data/todo/README.md` for the
schema before the first change in a session.

## Add

1. Make the slug from the title: lowercase words joined by `-`, such as
   `call-the-bank`. If the file exists, add `-2`.
2. Write the file with `title`, `status: open`, `created` (today) and only the
   fields the user gave. Do not invent a due date or a priority.
3. Use a tag only if it is in `tags.json`. If the user names a new tag, add it
   to `tags.json` first and say so.
4. Put details, links and subtasks in the body. Keep the title short.

## List

1. Find the open tasks: `grep -L "^status: done" data/todo/tasks/*.md`.
2. Read the frontmatter of each one, with `head -12`, not the whole file.
3. Sort by priority, then by due date, soonest first. A task with no due date
   comes last.
4. Show one line for each task: the title, the due date, the priority. Show the
   tasks that are past their due date first, and say that they are late.

When the user asks for one tag or one day, show only those tasks.

## Complete

Set `status: done` and add `done:` with today's date. Do not delete the file.
If more than one task matches what the user said, ask which one.

## Change

Edit only the field that the user changed. Never rename the file, because links
use the file name.

## Tasks from other work

When a source, a meeting or a dropbox file has a clear action for the user,
offer to add it as a task. Link the task to the page it came from with
`[[page-name]]`.
