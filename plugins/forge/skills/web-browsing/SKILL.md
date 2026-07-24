---
name: web-browsing
description: Use the browse CLI for webpages, with the Browserbase remote-session budget. Use whenever a task opens a URL or WebFetch returns a JavaScript shell.
user-invocable: false
---

# Web Browsing

`browse` drives real Chrome, locally or on Browserbase. Use it for any
real webpage. WebFetch is for raw files, JSON APIs, and plain text
only, and is never retried after returning empty content or a
JavaScript shell.

Run `browse skills show` before the first browse command in a session
and follow it for command mechanics. These rules apply on top.

- Pass the mode explicitly on every `browse open`. Use `--local` on a
  machine with Chrome. Use `--remote` when no local Chrome exists or
  the site needs Browserbase infrastructure.
- Give each independent task its own `--session <name>`. When
  `BROWSE_SESSION` is set, every command already targets that session.
  Pass no `--session`, and never stop it. The user owns it.
- Stop sessions you created when their task ends.
- Remote sessions need `BROWSERBASE_API_KEY` in the environment. Never
  print it, and never export a secret yourself. Sessions never need a
  project ID.
- Bot-protected sites need paid Browserbase features. Say so plainly
  and offer another source instead of retrying a block page.
- If the CLI is missing, do not install it. Fall back to WebFetch,
  complete the task as static HTML allows, and note the limitation in
  the report.

## Remote budget

Remote sessions spend a metered monthly budget of 100 browser hours.
Local Chrome is free, which is one more reason to prefer it. Before
opening a remote session, check usage:

```
browse cloud projects usage "$BROWSERBASE_PROJECT_ID"
```

When the variable is unset, derive the ID from
`browse cloud projects list`. A 404 means the stored ID is stale.
Re-derive it and tell the user the entry needs updating.

- Pace line: about 3 hours 20 minutes per day of the billing month.
  Ahead of pace, say so and lean harder on local mode.
- Past 80 hours, warn in every browsing report. Past 90, ask before
  any new remote session. At 100, stop. Overage needs an explicit go.
- Leaked sessions burn budget while idle. After remote work, confirm
  nothing is RUNNING with `browse cloud sessions list`. No `keepAlive`
  for one-off tasks. Prefer short timeouts so forgotten sessions end
  themselves.
