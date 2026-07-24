---
name: clean-architecture
description: Clean Architecture reference, reduced to this owner's positions and test-based enforcement. Use when scaffolding, reviewing layers, or designing a layered system.
user-invocable: false
---

# Clean Architecture

The textbook is assumed: four layers, dependencies point inward, ports
and adapters, composition at the entry point. This skill records where
this codebase's owner takes positions the textbook leaves open, and
how the rules are enforced by tests instead of prose.

## Positions

- **Ports are named for capability, never technology.**
  `UserRepository`, never `PostgresUserStore`. `Notifier`, never
  `SmtpClient`. The name must survive an implementation swap.
- **Use cases are verbs.** `PlaceOrder`, `DeactivateUser`. Never
  `UserService`. Generic CRUD names invite scope creep.
- **Entities never get interfaces "for flexibility."** A domain type
  with exactly one shape stays concrete. Wrapping it is indirection
  without payoff. Ports exist at the application boundary, for
  persistence, network, time, randomness, and I/O.
- **A domain test needing a mock is a design smell.** It proves the
  domain took on a dependency it should not have. Fix the dependency,
  never the test.
- **Web apps follow their framework.** Laravel, Rails, Django, and
  Next.js projects keep their own layout. Business logic still stays
  out of controllers and templates. Never force a four-layer tree onto
  a framework that fights it.

## Enforcement

Prose does not enforce the dependency rule. A fitness test does:
a test that fails when `domain/` or `application/` imports
infrastructure, presentation, or a framework package. Scaffolded
projects include one. In review, check imports first. An inner-layer
file importing outward is the violation, whatever the code does. When
the repo has a fitness test, trust it and spot-check. When it lacks
one, suggest adding it.

## Testing per layer

Domain: pure unit tests, no doubles. Application: unit tests with
fakes for ports. Infrastructure: integration tests against the real
dependency, because mocking the thing you integrate with defeats the
test. Presentation: request in, response out. A healthy suite is
mostly fast inner-layer tests with a thin ring of integration tests
at the seams.
