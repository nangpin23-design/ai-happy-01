"""Make the AI judge happy (ai-happy-01) — entry program.

Copies the entry image (entry.png, in this repository's root) to
/output/entry.png. Deterministic: no network, no randomness, both runs
write the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
