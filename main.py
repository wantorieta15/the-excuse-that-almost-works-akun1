# SPDX-License-Identifier: MIT
"""Entry generator for the Make Fun bounty
"The Excuse That Almost Works" (u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5).

Writes exactly one line of plain text -- the excuse a gamer texts their boss
to skip work during GTA 6 launch week -- to <out_dir>/entry.txt.

Pure Python standard library only: no network, no third-party dependencies.
The file is written directly (open + explicit chmod 0644); no atomic-write
helpers, so the grader can read it regardless of uid.
"""

import os

ENTRY = (
    "Badge reader died on my floor, IT ticket says Tuesday, "
    "and my laptop update is at 4% since 6am."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
