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

MAX_CHARS = 140
MAX_WORDS = 20


def build_entry() -> str:
    """Return the single entry line, validated against the bounty rules."""
    text = ENTRY
    validate_entry(text)
    return text


def validate_entry(text: str) -> None:
    """Enforce the bounty constraints on the entry line.

    One line, at most 20 words, at most 140 characters, no trailing
    newline, no leading/trailing whitespace.
    """
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "entry is %d words, over the %d limit" % (len(words), MAX_WORDS)
        )


def write_entry(out_dir: str) -> str:
    """Write the validated entry to <out_dir>/entry.txt, mode 0644."""
    text = build_entry()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
