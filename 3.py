"""
word_count.py
- 텍스트 파일의 단어 개수를 세는 간단한 유틸리티
- 사용법:
    python word_count.py example.txt
"""

import sys
from pathlib import Path

def count_words(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    words = text.split()
    return len(words)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python word_count.py <파일명>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print("파일을 찾을 수 없습니다.")
        sys.exit(1)

    num_words = count_words(file_path)
    print(f"{file_path.name} 파일의 단어 수: {num_words}")
