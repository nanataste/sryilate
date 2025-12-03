"""
number_guess.py
- 1부터 100 사이의 숫자를 맞추는 간단한 콘솔 게임
"""

import random

def number_guess_game():
    answer = random.randint(1, 100)
    attempts = 0
    print("=== 숫자 맞추기 게임 ===")
    print("1부터 100 사이의 숫자를 맞춰보세요!")

    while True:
        attempts += 1
        try:
            guess = int(input("숫자를 입력하세요 (종료: 0): "))
        except ValueError:
            print("숫자만 입력하세요!")
            continue

        if guess == 0:
            print("게임을 종료합니다.")
            break

        if guess < answer:
            print("더 큰 숫자입니다.")
        elif guess > answer:
            print("더 작은 숫자입니다.")
        else:
            print(f"정답입니다! 시도 횟수: {attempts}번")
            break

if __name__ == "__main__":
    number_guess_game()
