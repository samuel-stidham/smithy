---
name: test-harness
description: Generate an MCP server exposing the project's domain and application layers for headless testing.
argument-hint: "[optional focus area, e.g. \"the REST API endpoints\"]"
disable-model-invocation: true
---

# /forge:test-harness

Generate an MCP server that exposes this project's public API surface
as tools, so Claude can drive the application headlessly: launch it,
send inputs, read state, find bugs. This command builds the harness.
The QA pass is a separate task the user starts afterward.

Focus area: $ARGUMENTS. Empty means the full public API surface.

## Orientation

Detect the language and tooling from manifests. Never assume them.
Find the domain and application layers per the `clean-architecture`
skill. The harness wraps the same interfaces the presentation layer
uses, never infrastructure or presentation directly. If an MCP server
already exists in the project, ask before extending or replacing it.

## Generate

- A standalone module in the language's idiomatic layout, such as
  `cmd/mcp-server/` in Go or an `mcp-server/` package elsewhere. Stdio
  transport. The harness depends on the project. The project never
  depends on the harness.
- Tools in four groups, as the API surface supports them: lifecycle
  (start, stop, reset, configure), actions (send inputs, trigger
  operations, plus a batch tool to cut round trips), inspection
  (structured state, detailed and summary forms), and targeted testing
  (state overrides for edge cases, clearly marked test-only).
- An `mcpServers` entry in `.claude/settings.json`, merged into any
  existing file, never overwriting it.
- A `TEST_PLAN.md` checklist: general lifecycle checks, feature checks
  from the domain API, edge cases, and milestones. Prose per the
  `writing-style` skill.

## Workflow

State what you found and what you will wrap, briefly. Generate the
module, the config entry, and the test plan. Build and verify the
server starts using the project's own toolchain. Commit per the
`conventional-commits` skill. Report and suggest the QA pass next.

## Boundaries

No QA pass. No production-code changes. No push or PR. That is
`/forge:ship`.
