#!/usr/bin/env python3
"""Pickup Lines for Machines entry (make.fun program/v1).

Writes one original pickup line to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``). The line is a Wi-Fi
router speaking to another machine: signal, ping and packets as flirtation.
"""

import os

LINE = "Are you my Wi-Fi? Because my signal's never been stronger, my ping's never been lower, and I haven't dropped a packet since you walked in."

def main():
    # Gate guard: refuse to write a line outside the competition's gate
    # (UTF-8 text of 1-200 characters, not only whitespace, one line).
    if not 1 <= len(LINE) <= 200 or not LINE.strip() or "\n" in LINE:
        raise SystemExit("entry violates the 1-200 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
