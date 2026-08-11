---
name: change-control
description: Evidence and scope control for investigating, reviewing, proving, fixing, verifying, hardening, and refactoring software.
user-invocable: false
---

# Change Control

Evidence and scope rules for every verb that inspects or changes
code. They keep reviews and audits from quietly becoming speculative
fixes, broad hardening, refactoring, or cleanup. This skill owns
evidence and scope only. Code quality stays in `clean-code` and
layering in `clean-architecture`.

## Grading claims

Label every technical claim as exactly one of: observed fact,
inference, assumption, hypothesis, or verified conclusion. Never
present a lower grade as a higher one.

## The proof bar

A suspected bug is a hypothesis until all of these hold:

1. It names a violated requirement, invariant, contract, security
   boundary, or reproducible expected behavior.
2. It shows a reachable execution path.
3. It states the concrete preconditions that trigger it.
4. The existing protections along that path have been examined.
5. Deterministic proof exists, or a precise proof strategy does.

## Classifying findings

Every finding carries exactly one classification:

- **PROVEN BUG**. The proof bar is fully met.
- **STRONGLY SUPPORTED, REQUIRES PROOF**. Mechanism and path are
  clear. Proof is still owed.
- **UNPROVEN CONCERN**. Plausible and unverified.
- **HARDENING OPPORTUNITY**. No defect shown. Defense could improve.
- **MAINTAINABILITY COMMENT**. A quality observation, judged by
  `clean-code` or `clean-architecture`.
- **STYLE PREFERENCE**. Taste. Never blocking.

Only a PROVEN BUG, or a finding the user explicitly accepts, may
trigger a production change. Low-confidence and unproven findings
never do.

## Operating modes

Review, proof, fixing, verification, hardening, and refactoring are
separate modes. A verb runs only the modes its own file documents,
in the documented sequence. An explicitly invoked end-to-end verb
runs only that sequence. Never move implicitly from review, audit,
or proof into production changes. When another mode is needed, stop
and recommend its verb.

## Before editing production code

Report first:

- the objective
- the included scope and the exclusions
- the proof or acceptance evidence relied on
- the files expected to change
- the change budget in force
- the stopping condition

## The default repair budget

The budget bounds one fix. It does not bound a branch, a pull request,
or a release. Its purpose is to keep a single edit from sprawling into
unrelated code.

One fix addresses one independent problem, within:

- at most three production files
- at most 150 changed production lines
- no new dependency
- no public API, schema, or file-format change

An explicit user or repository instruction may override the budget.
Nothing else may.

## Batching fixes into a release

A branch, a pull request, and a release may each carry many fixes.
Releases normally bundle bug fixes, enhancements, and occasionally new
features. Nothing here requires one pull request per fix, and no verb
may imply otherwise.

Each fix is still scoped on its own:

- Work one problem at a time and finish it before starting the next.
- Keep each fix separable in the history, ideally its own commit.
- Verify each fix against its own evidence, never as a batch.
- Apply the budget to each fix, rather than summing it across the
  branch.
- Report the running list when several fixes land together, so a
  reviewer sees what each one covers.

Bundling is a packaging decision. Scoping is a correctness one. A
batch of fixes never licenses one sprawling edit.

## Stopping conditions

Stop and report, instead of editing or broadening, when any of
these appears:

- the claim cannot be proven
- the budget is insufficient
- a new dependency is required
- an API, schema, migration, or compatibility change surfaces
- a documented invariant must change
- an unrelated failure is discovered
- a single fix would grow to cover a second independent issue
- another operating mode is required

The last condition bounds one fix, not the branch it lands on. Finish
the fix in hand, report it, then open the next one.

## Verification never mutates

Verification observes the tree. Never run formatter, linter,
dependency, or code-generation auto-fix options while verifying. A
check that changes files is itself a finding to report.
