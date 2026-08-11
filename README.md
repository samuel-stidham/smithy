# smithy

smithy is a marketplace of lean, repo-agnostic plugins for
[Claude Code](https://claude.com/claude-code), ChatGPT, and Codex:
six plugins, one set of shared rules. It makes no assumptions about
language, framework, or tooling. Every verb detects what it needs
from the repo itself: manifest files, lockfiles, existing patterns,
and the repo's own agent instructions. It never requires per-repo
configuration.

## The family

| Plugin | What it does | Where it runs |
| --- | --- | --- |
| **forge** | Core engineering workflow: execute tasks, debug, refactor, evaluate options, review diffs, ship draft PRs, cut releases, generate test harnesses. | Enabled globally. |
| **foundry** | Product factory: scaffold complete Clean Architecture project templates, deploy them with OpenTofu. | Enabled per repo. |
| **draft** | Writing studio: books, poetry, technical articles, and repo documentation, with adversarial prose review and ebook compilation. | Enabled per repo. |
| **anvil** | Nix environments: shell gates, distro-family portability audits, devenv environments, confirmed activation. | Enabled per repo. |
| **bellows** | Recurring automation: scheduled routines, watches over long-running work, CI pipelines, dependency upgrades. | Enabled per repo. |
| **temper** | Security: repo-wide audits across secrets, dependencies, code, and configuration, then hardening in exploitability order. | Enabled per repo. |

foundry, draft, anvil, bellows, and temper require forge. They
borrow its shared skills by name (`forge:clean-architecture`,
`forge:writing-style`, `forge:citations`, `forge:web-browsing`,
`forge:adversarial-review`). Claude Code installs forge
from the dependency declared in each leaf manifest. ChatGPT and Codex
users install forge first; the OpenAI plugin manifest does not expose
Smithy's plugin-to-plugin dependency.

## Installation

### Claude Code

```text
/plugin marketplace add samuel-stidham/smithy
/plugin install forge@smithy
/plugin install foundry@smithy
/plugin install draft@smithy
/plugin install anvil@smithy
/plugin install bellows@smithy
/plugin install temper@smithy
```

Install forge at user scope so it is available everywhere. Keep the
leaves disabled globally and enable them per repo: draft in writing
projects, foundry where products get built or deployed, anvil in
machine definitions and devenv projects. bellows goes wherever
unattended jobs run, and temper wherever the code faces users or
handles secrets. One line in that repo's
`.claude/settings.local.json` does it, or use the `/plugin` menu.

### Codex and ChatGPT

Add the Git marketplace and install forge before any leaf plugin:

```text
codex plugin marketplace add samuel-stidham/smithy --ref main
codex plugin add forge@smithy
codex plugin add foundry@smithy
codex plugin add draft@smithy
codex plugin add anvil@smithy
codex plugin add bellows@smithy
codex plugin add temper@smithy
```

Use `/plugins` to browse the marketplace in Codex CLI. The same repo
marketplace appears in ChatGPT Work or Codex in the desktop app when
the checkout is the active project. Start a new chat or Codex session
after installing a plugin.

## Updating

Claude Code:

```text
/plugin marketplace update smithy
```

Then update the plugin from the `/plugin` menu and restart Claude
Code. Each plugin versions independently, tagged
`{plugin}--v{version}`.

Codex:

```text
codex plugin marketplace upgrade smithy
codex plugin add forge@smithy
```

Repeat the install command for each enabled leaf plugin, then start a
new session.

## forge

Invoke a verb as `/forge:<name>` in Claude Code,
`$forge:<name>` in Codex, or `@forge:<name>` in ChatGPT:

- **do-work** executes a development task end to end. It orients in
  the repo, shows a short plan, branches, implements through capped
  implementer subagents, tests with the repo's own tooling, and
  reports with a suggested PR title and body. It stops before
  pushing.
- **debug** takes a symptom to a proven fix. It reproduces first,
  isolates by shrinking and bisecting, and names the root cause
  apart from the trigger that revealed it. The regression test runs
  both ways before it counts. If nothing proves the symptom, it
  stops with zero production changes.
- **prove** takes exactly one finding to a verdict: proven, or
  rejected and downgraded. It never modifies production code, and
  it stops after the proof instead of fixing anything.
- **verify** runs the repo's own QA checks, narrowest to broadest,
  in check-only modes. It introduces no changes, and a check that
  mutates files is itself a reported finding.
- **refactor** restructures code without changing behavior. It
  builds the safety net first, writing characterization tests where
  coverage is thin. Then it moves in small commits that each pass
  the full suite. A bug found mid-refactor gets reported, never
  silently fixed.
- **evaluate** answers one engineering decision with evidence: cited
  research per `citations`, an optional throwaway spike, and exactly
  one recommendation. Runners-up get the reason they lost.
- **review** audits the current branch's diff against its base
  through six lenses: architecture, code quality, tests, security,
  docs, and scope. Claude runs it in an isolated subagent; other
  hosts preserve its read-only boundary. It ends with exactly one
  verdict: **SHIP IT**, **NEEDS WORK**, or **RETHINK**.
- **ship** runs pre-flight checks, pushes the branch, and opens a
  draft PR with a What/Why/How/Testing body built from your actual
  commits. Without `gh` it still pushes and prints a copy-ready body.
- **version** cuts a release: bump, changelog, annotated tag, push
  the tag. In a plugin marketplace monorepo it asks which plugin and
  tags that plugin's release in the format documented under
  Updating. It always confirms before tagging.
- **test-harness** generates an MCP server exposing the project's
  domain and application layers as tools, so the active coding agent
  can drive the app headlessly for QA. It builds the harness only.
- **eval** runs scripted behavioral scenarios against plugin verbs
  in headless sessions, one fresh scratch repo per scenario. Tree
  hashes decide whether a boundary held, and transcripts get graded
  against the verbs' own documented rules. Claude loads the package
  under test directly; Codex uses ephemeral `codex exec --json`
  sessions and verifies each required plugin is installed, enabled,
  and current before it runs. Scenario files live in the repo's
  `evals/` directory.

The shared reference skills, loaded by name: `adversarial-review`
(the hostile fresh-context reviewer every review verb dispatches
through, with lens packs per artifact class, severity findings, and
one verdict), `clean-architecture` (the owner's positions plus
test-based enforcement of the dependency rule), `clean-code`
(judgment cues over metrics), `change-control` (evidence grades,
finding classifications, the default repair budget, and stopping
conditions), `citations`
(verified, reader-accessible sources in APA style, with
reference-ledger support), `conventional-commits` (commit and PR
title format), `writing-style` (the rules that keep prose human),
and `web-browsing` (the browse CLI, with a Browserbase remote-session
budget).

### Security layers

Security runs in three layers, each with its own timing, and forge
owns only the middle one. Anthropic's official `security-guidance`
plugin watches every edit in real time. It runs pattern warnings on
edits, an LLM diff review each turn, and an agentic commit review.
`/forge:review` applies the repo-specific security judgment no
general scanner has, and reports whether `security-guidance` covers
the session. `claude-security`, Anthropic's official multi-agent
scanner, is the deep on-demand pass before a release, and
`/forge:version` recommends it for deployable repos. smithy bundles
neither official plugin and never assumes they are installed. It
detects and defers. `/temper:audit` stays the repo-wide posture
audit, outside these diff-and-release layers.

## foundry

- **scaffold** generates a complete, working Clean Architecture
  project: layered structure with a dependency-rule fitness test, a
  multi-stage Dockerfile, compose, Makefile, CI, `.env.example`,
  README, per-layer example tests, and an MIT license. Types:
  `rest-api`, `cli-tool`, `background-worker`, `webhook-gateway`,
  `task-runner`, and `web-app` (which follows its framework's own
  conventions). Any language, using its real idioms.

  ```text
  /foundry:scaffold go rest-api
  /foundry:scaffold php web-app --infra opentofu --provider digitalocean
  ```

  `--infra opentofu` adds an `infra/` directory built to the
  `infrastructure-as-code` skill: modules named by role, provider
  abstraction across `aws`, `gcp`, and `digitalocean`, remote state,
  and secrets handling.
- **deploy** applies a repo's existing infrastructure: image build
  and push when a Dockerfile exists, plan-before-apply OpenTofu, the
  app's own release steps, then verification. It never destroys
  infrastructure and never prints secrets.

## draft

- **write** produces long-form prose in the project's own voice:
  fiction, nonfiction, poetry, or technical articles. It orients in
  the repo first and follows any publication target spec the project
  defines (fields, format, storage). Manuscripts follow the
  `creative` skill. Articles follow `technical-writing`, with
  research through `forge:web-browsing` and claims cited per
  `forge:citations`.

  ```text
  /draft:write chapter 3: the city falls and the survivors regroup
  /draft:write the elegy for the fallen city --type-poetry
  /draft:write article: what self-hosting CI taught me --type-article
  ```

- **publish** compiles a writing project into publishable EPUBs for
  Amazon KDP and Barnes and Noble Nook, validated against KDP's
  expectations. It builds local files only and never uploads. Needs
  [Pandoc](https://pandoc.org/installing.html) or an equivalent EPUB
  tool.
- **docs** writes repo documentation verified against the code it
  describes: READMEs, ADRs, API references, and guides. Commands
  shown in a doc get run when safe, and unrun ones are marked.
- **review** runs a hostile expert read of prose files through
  `forge:adversarial-review` with the prose lens pack. The lenses:
  factual accuracy, citation integrity, steelman integrity, writing
  style, and continuity. It reports severity findings and one
  verdict, and it never edits.

## anvil

- **check** runs the static gate over a Nix repo: every shell file
  checked with the right parser for its dialect (shellcheck cannot
  parse fish, so fish gets `fish -n`), then the flake or
  configuration evaluated. Builds nothing, changes nothing.
- **portability** audits shell and package selection against the
  distro families the repo claims. Every finding carries a file, a
  line, the family it breaks on, and a loud-or-silent verdict.
  Findings from families the machine did not run are marked
  unverified.
- **env** creates or updates a [devenv](https://devenv.sh/)
  development environment, reading the devenv option docs before
  writing a line, every time. Detects languages from manifests,
  writes `devenv.nix`, `devenv.yaml`, and the direnv `.envrc`, and
  evaluates before reporting success.
- **switch** builds a machine definition, shows the closure diff
  against the current generation, and activates only after
  confirmation. Prints the rollback command on failure. Never runs
  `sudo`, never bootstraps.

## bellows

- **routine** turns a recurring chore into a scheduled job with a
  full definition: purpose, cadence, boundaries, report destination,
  stop procedure. It dry-runs the job attended before registering it
  on whatever scheduler the environment offers.
- **watch** babysits long-running external work until it resolves: a
  PR moving through CI and review, a deploy, a migration. It reports
  transitions, stays quiet on green, and never makes the decision
  the human is watching for.
- **ci** authors or updates the repo's CI pipeline on the provider
  the repo already uses, mirroring the gates developers run locally.
  Secrets stay in the provider's secret store.
- **upgrade** moves dependencies in risk-ordered batches, testing
  after each. Majors get their changelogs read through
  `forge:web-browsing` first, and deliberate pins stay pinned.

Every unattended job is judged against the `automation-boundaries`
skill: no default-branch pushes, no merges, no publishing, loud
failure, idempotent runs.

## temper

- **audit** reads the repo's security posture without changing it.
  It covers secrets in tree and history, dependencies through the
  ecosystem's own audit tool, code at trust boundaries, and
  configuration. Findings rank by exploitability, and everything the
  audit skipped gets named.
- **harden** fixes exactly one proven finding per invocation, using
  its existing proof as the acceptance test. Changes to
  authentication, authorization, crypto, and session handling get
  confirmed before they land. A leaked credential gets reported for
  human rotation, never rotated by the plugin.

Both verbs share the `security-baseline` skill: exploitability
ranking, the secrets bar, validated trust boundaries, fail-closed
defaults, and audit honesty.

## Why this exists

forge exists to run multiple independent ventures off one consistent
workflow instead of rebuilding process for each new project. The core
verbs are how work gets planned, built, and shipped, whatever the
project. foundry is the engineering backbone behind a template
business. draft carries the books and the blog. Each new venture
starts from a working process instead of from zero, and every one of
them writes, commits, and ships by the same rules.

## Scope

forge is built for professional and personal development work, not
for academic use. Do not use it to complete coursework, assignments,
or exams. If you are unsure whether AI-assisted tools are allowed,
check your institution's academic integrity policy.

## License

MIT. See [LICENSE](LICENSE) for the full text.

## Inspiration

forge began as a leaner answer to
[Shipyard](https://github.com/mattsears18/shipyard), an autonomous
engineering loop plugin for Claude Code. The two have since diverged
in philosophy, and adopting Shipyard is no longer the growth path.
Shipyard scales autonomy: parallel worker pools, autonomous triage,
auto-merging PRs. smithy constrains it. Reviews and audits are
read-only, fixes require proof, automation never merges or
publishes, and every verb stops at a documented boundary. The bet:
one disciplined, evidence-gated process, identical on every host,
beats a faster loop with fewer brakes.
