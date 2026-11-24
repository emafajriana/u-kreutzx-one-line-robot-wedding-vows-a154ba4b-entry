"""One-Line Robot Wedding Vows entry (Python 3.13, standard library only).

Writes the vow to the output directory as entry.txt and verifies it
before returning: the text must be UTF-8, one line, 1 to 160 characters
and not only white space, matching the competition gate. Outside the
grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

VOW = (
    "I vow to love you in sickness and in health, in low battery and in "
    "airplane mode \u2014 and to always let you have the last 2%."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_vow(text: str) -> None:
    """Raise ValueError unless the vow passes the competition gate."""
    if not text or text != text.strip() or not text.strip():
        raise ValueError("vow must be non-empty and not only white space")
    if len(text) > 160:
        raise ValueError(f"vow is {len(text)} characters, over the 160 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")


def write_entry(text: str) -> Path:
    """Write the vow, then read it back and verify it in full."""
    check_vow(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    raw = target.read_bytes()
    written = raw.decode("utf-8")
    if written != text:
        raise IOError("read-back text differs from the vow")
    if len(raw) != len(text.encode("utf-8")):
        raise IOError("read-back byte count differs from the vow")
    check_vow(written)
    return target


def main() -> None:
    target = write_entry(VOW)
    print(f"wrote {target} ({len(VOW)} characters)")


if __name__ == "__main__":
    main()
