---
name: query
description: Answer a question against the wiki by reading the index, drilling into relevant pages, synthesizing with citations, and offering to file the answer back as a synthesis page. Use when the user asks a substantive question about the wiki's contents (patterns, connections, comparisons, "what does the wiki say about X").
---

# query

Answer a question from the pages. The goal is more than an answer: good
answers become new pages, so the wiki keeps growing.

## Flow

1. **Read the index of the area first.** `pages/world/index.md` for a question
   about other people's work, `pages/self/index.md` for one about the user,
   `pages/work/index.md` for a client or a build. Do this even when you think
   you know the pages. The index shows what you forgot.
2. **Read the pages it points to.** For a synthesis question, read many pages
   quickly, not one page in full.
3. **Answer with links.** Link each claim to its page with a `[[wiki-link]]`.
   When a claim is your inference and not a quote, say so: "[[a]] and [[b]]
   say X, which suggests Y."
4. **Show contradictions and gaps.** If two sources disagree, say so. If the
   pages cannot answer, say so. Do not fill the gap with a guess.
5. **Offer to save it.** At the end, ask if the answer should become a page in
   `pages/world/concepts/`, or in `pages/world/comparisons/` for an A against B
   comparison. Save it only when the user says yes, or when the user asked for
   it at the start.

## When an answer is worth a page

- It connects three or more pages that had no connection.
- It shows a pattern that you would otherwise work out again later.
- It compares two or more things on the same points.

Do not save a simple lookup, or an answer that repeats a page that exists.

## Saving it

1. Pick the folder: `pages/world/concepts/` for a pattern,
   `pages/world/comparisons/` for a comparison, or an update to an existing
   page if the answer belongs there.
2. Add one line for it in the index of the area.
3. Add an entry to `pages/log.md`, with the pages that it came from:
   ```
   ## [YYYY-MM-DD] query | <question>
   ```
4. Add a link to the new page from each page that it came from.

## Do not

- Do not answer from memory when the pages have the answer. Read the files.
