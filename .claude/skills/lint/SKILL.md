---
name: lint
description: Health-check the wiki. Find contradictions, stale claims, duplicate pages, orphan pages, missing cross-references, and disambiguation gaps. Use when the user says "lint the wiki", "clean up the wiki", or after a bulk-ingest session.
---

# lint

Check the health of the wiki, as `MIND.md` says. The goal is to make the pages
that exist better, not to add new material.

## Scan

Read the index of each area first. Then read concept and entity pages as you
need them. Do not read every file. Read enough to make the list of problems.

## Problems to look for

1. **Duplicate concepts:** two or more pages about the same pattern under
   different names. Propose a merge: the page to keep, the pages to merge into
   it, what to keep from each.
2. **Duplicate entities:** one tool, person or company under two names, such
   as `notion.md` and `notion-so.md`. Name the one to keep.
3. **Orphan pages:** pages that no other page links to.
4. **Contradictions:** two pages that disagree and do not say so. Show them.
   Do not choose a side.
5. **Old claims:** a claim that a newer source replaced, or a page that says
   "one case only" when more cases are now on other pages.
6. **Missing links back:** page A links to B, but B does not link to A.
7. **Same first name:** two different people with the same first name, and no
   note on either page to tell them apart.
8. **Missing pages:** a `[[link]]` with no page, or a subject named in three
   places with no page of its own.

## Report

Make a report, and change nothing yet:

```
## Duplicate concepts (N)
- [[a]] + [[b]] → merge into [[a]]. Keep: ... Delete: ...

## Contradictions (N)
- [[p1]] says X. [[p2]] says not X.

## Missing links back (N)
- [[a]] → [[b]]. Add a link back in [[b]].
```

Ask the user which items to fix. Merge, delete or add links only after the user
says yes.

## Fix

- **Merge:** rewrite the page to keep, so that it has the content of each
  duplicate. Delete the duplicates. Update the index and each link to a deleted
  page.
- **Delete:** delete the file and remove it from the index.
- **Links back and notes:** add one line to the page.

Add a `## [YYYY-MM-DD] lint` entry to `pages/log.md` that says what you did.
