"""
rock_paper_scissors.py
- 콘솔에서 하는 간단한 가위바위보 게임
"""

import random

CHOICES = ["가위", "바위", "보"]

def get_result(user, computer):
    if user == computer:
        return "비겼습니다!"
    if (
        (user == "가위" and computer == "보") or
        (user == "바위" and computer == "가위") or
        (user == "보" and computer == "바위")
    ):
        return "이겼습니다!"
    return "졌습니다..."

def main():
    print("=== 가위바위보 게임 ===")
    print("그만하려면 '종료'를 입력하세요.")

    while True:
        user = input("가위 / 바위 / 보 중 하나를 입력: ").strip()
        if user == "종료":
            print("게임을 종료합니다.")
            break
        if user not in CHOICES:
            print("잘못된 입력입니다. '가위', '바위', '보' 중에서 골라주세요.")
            continue

        computer = random.choice(CHOICES)
        print(f"컴퓨터: {computer}")
        print(get_result(user, computer))
        print()

if __name__ == "__main__":
    main()
