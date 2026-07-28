---
name: shell-portability
description: The distro-family trap list for script shell. Use when auditing portability across Debian, RHEL, Arch, and ostree families.
---

# Shell Portability

The standing trap list for script shell across distro families.
Every entry came from a failure already observed on a real machine.
Report each hit with its family and whether it fails loudly or
silently. Where this list does not record loudness, verify on the
machine before asserting it. Silent failures outrank loud ones.

- Debian multiarch libdirs against `/usr/lib64` on RHEL-family
  layouts. A path built for one misses on the other.
- `/usr/bin` against `/usr/sbin` for privileged binaries. Families
  merge or split them differently.
- `/media/$USER` against `/run/media/$USER` for udisks mounts.
- A read-only `/usr` under ostree systems (Silverblue and kin).
- `case` statements with no default arm. The unmatched family falls
  through silently and the function returns success.
- GNU-only flags on `find`, `sed`, `stat`, and `date`.
- A `pkg_install` return value that kills the script under `set -e`,
  far from the cause.

The adjacent trap is package naming, owned by the `parity` skill:
read every distro package name off that distro's package database
through `forge:web-browsing`, never from memory. The difference
between `btrfs-progs` and `btrfsprogs` is one hyphen and a failed
install on a machine nobody can test.
