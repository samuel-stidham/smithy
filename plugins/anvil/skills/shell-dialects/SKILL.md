---
name: shell-dialects
description: Differences between bash, fish, and zsh - parsers, pipeline status indexing, process substitution, exports, startup files. Use when checking or porting shell.
user-invocable: false
---

# Shell Dialects

The differences between bash, fish, and zsh that break ported
scripts. `portability` asks which distro breaks. This skill answers
the other question: which parser to run and which semantics apply.

Shell is two subjects, never one. **Script shell** is what `*.sh`
files and `writeShellApplication` derivations produce, bash in
practice, running unattended, owned by shellcheck. **Interactive
shell** is whatever login shell the configuration declares, plus its
config tree, where real logic often lives: status gates, process
substitution, secret loading. shellcheck sees none of it.

- **Parsers.** shellcheck cannot parse fish. On valid fish it exits
  1 and reports `SC1073 Couldn't parse this function`, so its
  findings on fish are false errors on correct code. Gate fish with
  `fish -n` (exit 0 clean, 127 on a syntax error) and zsh with
  `zsh -n` (exit 1 on a syntax error). Measured 2026-07-24 on one
  Linux workstation. Unverified elsewhere.
- **Pipeline status indexing.** bash `$PIPESTATUS` is zero-indexed:
  the first command is `[0]`. fish `$pipestatus` is one-indexed: the
  first command is `[1]`. zsh carries both, which is worse than
  carrying either. A script ported between them reads a real exit
  status from the wrong command and reports success. Measured
  2026-07-24, same caveat. This entry leads because the failure is
  silent and costly.
- **Process substitution.** `<(...)` in bash and zsh. It does not
  exist in fish, which needs `psub`: `-F` is the fifo, `-f` the
  default regular file.
- **Status and export.** `$?` against `$status`. `export VAR=x`
  against `set -gx VAR x`.
- **Startup files.** The login, interactive, and neither matrix
  decides which file runs. The systemd trap is its general form: a
  variable set in an interactive profile is invisible to anything a
  timer starts.
