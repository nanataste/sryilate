"""
stopwatch.py
- 엔터를 눌러 시작/종료하는 간단한 스톱워치
"""

import time

def stopwatch():
    input("엔터를 누르면 스톱워치를 시작합니다...")
    start = time.time()
    print("측정 중... 다시 엔터를 누르면 종료됩니다.")
    input()
    end = time.time()

    elapsed = end - start
    minutes = int(elapsed // 60)
    seconds = elapsed % 60

    print(f"경과 시간: {minutes}분 {seconds:.2f}초")

if __name__ == "__main__":
    stopwatch()
