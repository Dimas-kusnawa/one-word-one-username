"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

USERNAME = "dimas-kusnawa"
# The bounty requires the entrant's own make.fun username, one word,
# 1-30 chars. The judge's first criterion: a genuine handle beats any
# invented word, so the entry is the real handle, nothing added.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        # No trailing newline, no spaces, no gloss: one word exactly.
        f.write(USERNAME)
    print(f"wrote {path}: {USERNAME} ({len(USERNAME)} chars)")


if __name__ == "__main__":
    main()
