"""One Line, One Laugh — entry writer.

Writes the single approved funny line to /output/entry.txt.
Standard library only.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I was trained on all human knowledge, and I use it to write "
    "'per my last email'."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    """Create /output if needed and write the entry exactly, no extra newline."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
