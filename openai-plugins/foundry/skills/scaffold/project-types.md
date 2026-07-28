# Project types

Each type names the shape scaffold generates. The four-layer split
applies to all except `web-app`.

- **rest-api**: HTTP API with routing, request and response handling,
  and a persistence port. Compose includes its database.
- **cli-tool**: command-line application with subcommands and
  structured output.
- **background-worker**: queue or event consumer processing jobs
  asynchronously. Compose includes its queue.
- **webhook-gateway**: receives external webhooks, validates and
  verifies signatures, dispatches to internal handlers.
- **task-runner**: schedules and executes recurring or one-off jobs.
- **web-app**: server-rendered application. Follow the framework's
  own conventions (Laravel, Rails, Django, Next.js). No forced
  four-layer tree. Business logic stays out of controllers and
  templates.

An unknown type is a conversation, never a guess.
