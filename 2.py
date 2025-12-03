"""
todo_cli.py
- 아주 간단한 텍스트 기반 To-Do 리스트
- 사용법 예시:
    python todo_cli.py add "파이썬 공부하기"
    python todo_cli.py list
    python todo_cli.py done 1
"""

import sys
from pathlib import Path

DATA_FILE = Path("todo.txt")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

def cmd_list():
    tasks = load_tasks()
    if not tasks:
        print("할 일이 없습니다 :)")
        return
    print("=== To-Do 리스트 ===")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def cmd_add(text):
    tasks = load_tasks()
    tasks.append(text)
    save_tasks(tasks)
    print(f"추가됨: {text}")

def cmd_done(index_str):
    try:
        index = int(index_str) - 1
    except ValueError:
        print("번호는 숫자로 입력하세요.")
        return

    tasks = load_tasks()
    if not (0 <= index < len(tasks)):
        print("해당 번호의 할 일이 없습니다.")
        return

    finished = tasks.pop(index)
    save_tasks(tasks)
    print(f"완료 처리됨: {finished}")

def print_help():
    print("사용법:")
    print("  python todo_cli.py list")
    print('  python todo_cli.py add "할 일 내용"')
    print("  python todo_cli.py done 번호")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
    else:
        command = sys.argv[1]

        if command == "list":
            cmd_list()
        elif command == "add" and len(sys.argv) >= 3:
            cmd_add(" ".join(sys.argv[2:]))
        elif command == "done" and len(sys.argv) == 3:
            cmd_done(sys.argv[2])
        else:
            print_help()
