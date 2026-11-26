"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one line about office life to /output/entry.txt.
"""
import os

JOKE = "Our office has a 'no-meeting Fridays' policy, so we moved Friday's meeting to Thursday and renamed it 'Pre-Friday Alignment'."


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)


if __name__ == "__main__":
    main()
