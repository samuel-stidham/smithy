# Changelog

## temper--v0.2.1

### Changed

- audit drops the connector colon from its read-only rule and a
  propping adverb.
- Skill headings move to sentence case per the writing-style rule.

## temper--v0.2.0

### Changed

- audit applies `forge:change-control`: shared claim grades and
  classifications, no unproven claim called a vulnerability, and at
  most one recommended next proof.
- harden accepts exactly one proven finding per invocation and uses
  its proof as the acceptance test. The quick-audit-then-fix path is
  removed. No finding routes to `/temper:audit`, and an unproven one
  routes to `/forge:prove`.

## temper--v0.1.0

Initial implementation of the temper design: the audit and harden
verbs, plus the security-baseline reference skill.
