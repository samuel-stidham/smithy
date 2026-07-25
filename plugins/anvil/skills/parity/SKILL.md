---
name: parity
description: The standard a machine definition is judged against - feature, package, software, and configuration parity across families. Owns the package-name rule and the honesty rule.
user-invocable: false
---

# Parity

The bar a machine definition is judged against: feature, package,
software, and configuration parity across every family it claims.
Parity means the same machine, never merely a run that did not
crash. A function that installs nothing on one family and returns
zero passes a smoke test and fails this standard.

## The package-name rule

Every distro package name is read off that distro's package database
through `forge:web-browsing`, never recalled from memory. Model
memory of package names is stale and confidently wrong.

## The honesty rule

anvil runs on one machine at a time and can only execute against the
family it is standing on. Every finding about a family it did not
run on is marked unverified, in the report and in any commit body it
drafts. A confident guess gets trusted, and that is the failure mode
this plugin exists to prevent.
