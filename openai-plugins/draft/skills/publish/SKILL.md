---
name: publish
description: Compile a writing project into publishable ebook formats, EPUB for KDP and Nook. Local files only, no uploads.
---

# draft:publish

Compile a writing project into publishable ebook files. The prose
counterpart of `forge:ship`: it builds the manuscript into files
ready for upload to KDP and Nook, and never uploads. This plugin
requires forge.

Requested format or platform: the user's request. Strip context flags first
(the `creative` skill defines them). Nothing remaining means all
supported formats.

## Orientation

- Find the book metadata: title, author, description, language, any
  ISBNs. Missing metadata is a question, never a guess.
- Establish chapter order from a table of contents, outline, or
  numbered files. Ambiguous order is a question.
- Find the cover image. None means a note in the report, never a
  generated one.
- Place front matter and back matter correctly when present.

## Formats

EPUB is the primary output. KDP and Nook both accept it. Validate
against KDP's metadata, table-of-contents, and cover expectations.
MOBI only on explicit request.

## Workflow

1. Assemble the manuscript in reading order. Text you adjust follows
   the `creative` skill, honoring any flags.
2. Apply typographic formatting: chapter headings, spacing, italics
   and bold preserved from the source.
3. Generate the EPUB with Pandoc or a similar available tool,
   embedding the cover and metadata. Missing tooling means install
   instructions for the user's platform, never silent failure.
4. Validate with `epubcheck` when available. Fix what is fixable and
   report the rest. Without it, note that manual validation is
   needed before upload.
5. Output to `dist/` or `build/`, never committed. Add the ignore
   entry when the `.gitignore` lacks it.
6. Report per `forge:writing-style`: what was generated, where, file
   sizes, validation results, and the per-platform checklist (KDP at
   kdp.amazon.com, Nook at press.barnesandnoble.com).

## Boundaries

No uploads. No pricing, categories, or keywords. No cover art. No
committing build artifacts.
