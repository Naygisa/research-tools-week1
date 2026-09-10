"""Count English word frequencies in a UTF-8 text file."""

import re
import sys
from collections import Counter
from pathlib import Path


def count_words(text):
    """Return English word frequencies, ignoring letter case."""
    words = re.findall(r"[A-Za-z]+", text.lower())
    return Counter(words)


def main():
    if len(sys.argv) != 2:
        print(f"用法: python {Path(sys.argv[0]).name} <文本文件路径>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    try:
        text = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"错误：文件不存在：{input_path}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"错误：无法读取文件 {input_path}：{error}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print(f"错误：文件不是有效的 UTF-8 文本：{input_path}", file=sys.stderr)
        return 1

    for word, count in sorted(count_words(text).items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}: {count}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
