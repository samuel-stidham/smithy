---
name: security-baseline
description: The standard a repo's security posture is judged against. Exploitability ranking, the secrets bar, trust boundaries, and audit honesty.
user-invocable: false
---

# Security Baseline

The bar audit findings and harden fixes are both judged against.

## Exploitability ranks findings

Reachable beats theoretical. A finding an attacker can reach today
outranks a scarier one behind three preconditions. Severity labels
from tools are inputs to this ranking, never the ranking itself.

## The secrets bar

No plaintext secret in the tree, the history, the logs, or any
report this plugin writes. Secrets load through the environment's
secret mechanism, whatever it is. A found secret stays critical
until the human confirms rotation.

## Trust boundaries

Everything crossing into the system gets validated. Everything
crossing out gets encoded for where it lands. Authorization is
checked where the resource is touched, never only at the edge.

## Fail closed

When a security control cannot decide, it denies. A parser,
authorizer, or validator that fails open is a finding on its own.

## The honesty rule

Every unverified claim is marked unverified. Every area the audit
skipped is named. A scanner that ran clean is evidence, never a
verdict, and a report never inflates confidence to look thorough.
