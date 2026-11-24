#!/usr/bin/env python3
"""The One-Line Laugh - a program that writes one funny line to /output/entry.txt.

One sentence, at most 200 characters: a setup with a triple escalation and a
surprise at the end that still makes sense - an everyday truth about late-night
snacking and being broke.
"""

import os

LINE = "My smart fridge texted me I'm out of milk, out of money, and — judging by the midnight ice cream — out of excuses."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
