#!/usr/bin/env python3
"""Invent a Word We Need — entry generator.

Coins one new English word and defines it in a single clear line,
then writes the entry text to /output/entry.txt.
Deterministic: running this script twice produces byte-identical output.
"""

import os

# The word: "appnesia" — app + amnesia. A blend English could plausibly
# have grown on its own: short, spellable, sayable, instantly understood.
ENTRY = (
    "Appnesia: picking up your phone for a reason, "
    "then forgetting it the moment the screen lights up."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
