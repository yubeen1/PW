import os
import pickle


#사용자 정의 함수부
def input_scores():
    s = []
    i = 1
    while (True):
        n = int(input(f"#{i}? "))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

#주 프로그램부
filename = "score.bin"

if os.path.exists(filename):
    print("[파일 읽기]")
    with open(filename, "rb") as file:
        scores = pickle.load(file)

    print("\n[점수 출력]")
    print('개인점수:', end='')
    show_scores(scores)
    print(f"평균: {get_average(scores):.1f}")
else:
    print("[점수 입력]")
    scores = input_scores()

    print("\n[점수 출력]")
    print('개인점수:', end='')
    show_scores(scores)
    print(f"평균: {get_average(scores):.1f}")

    with open(filename, "wb") as file:
        pickle.dump(scores, file)
