"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

LINE = (
    "My gym membership works out to $48 a visit — more than the taxi "
    "I take there so I don't have to walk to the place where I pay to walk."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
