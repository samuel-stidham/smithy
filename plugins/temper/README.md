# temper

Tempering is the deliberate hardening pass after the piece is
formed. temper does the same for a repo. Audit the security
posture, then harden what the audit finds, in the order an attacker
would care about.

**Requires the forge plugin.** temper borrows `forge:writing-style`,
`forge:conventional-commits`, and `forge:web-browsing` by name.

- `/temper:audit`: repo-wide security audit across secrets,
  dependencies, code at trust boundaries, and configuration.
  Read-only, ranked by exploitability.
- `/temper:harden`: fix the findings, one commit each, tests after
  every fix. Risky changes get confirmed before they land.

The `security-baseline` reference skill is the standard both verbs
share: exploitability ranking, the secrets bar, trust boundaries,
fail-closed defaults, and audit honesty.

temper never rotates a credential and never pushes. Rotation touches
external systems, so it stays human. Enable per repo, wherever the
code faces users or handles secrets.
