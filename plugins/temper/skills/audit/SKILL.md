---
name: audit
description: Repo-wide security audit across secrets, dependencies, code at trust boundaries, and configuration. Read-only, ranked by exploitability.
argument-hint: "[optional scope, defaults to the whole repo]"
disable-model-invocation: true
---

# /temper:audit

Audit the repo's security posture and report what an attacker would
use. Read-only. Findings are the deliverable, and fixes are
`/temper:harden`. The `security-baseline` skill is the standard
every finding is judged against. The `forge:change-control` skill
supplies the claim grades, the proof bar, and the classifications.

The scope is: $ARGUMENTS. If empty, the whole repo.

## Setup

Read the repo's agent instructions and README, then detect the
ecosystem from manifests and lockfiles. Never assume tooling.

## Passes

Work each pass separately. Cite file and line. No generic advice.

- **Secrets.** Scan the tree and history with the scanners the repo
  or machine already configures, such as gitleaks or trufflehog.
  Without them, search by judgment and say the scan was manual.
- **Dependencies.** Run the ecosystem's own audit tool, detected
  from the manifests. A direct dependency weighs more than a
  transitive one.
- **Code.** Trust boundaries: injection, missing validation,
  authorization gaps, unsafe deserialization, crypto misuse. Deeper
  and wider than the diff-scoped security lens in `/forge:review`.
- **Configuration.** Debug flags on production paths, permissive
  CORS, public storage, over-broad access in any infrastructure
  code.

## Report

Rank by exploitability per the `security-baseline` skill. Reachable
beats theoretical. For each finding: file, line, how an attacker
reaches it, its `forge:change-control` classification and evidence,
and what harden should do about it. Never call an unproven claim a
vulnerability. Mark every unverified claim. Name what the audit did
not examine. A clean tool pass is a fact, never a verdict. End by
recommending at most one next proof through `/forge:prove`.
