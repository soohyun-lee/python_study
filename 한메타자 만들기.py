# #타이핑 게임 만들
import time
import random



WORD_LIST = [
    "지리산 맑은 샘물은 맛있다",
    "오늘은 밤이 늦었으니 그만 자렴",
    "파이썬은 코드가 짧고 유연하며 가독성이 좋다"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1
    tot_len = len(q)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = correct / end_time * 60

    print(f'속도 {speed:0.2f} 정화도 {c:0.2f} 오타율 {e:0.2f}')