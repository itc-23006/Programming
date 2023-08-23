import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good morning",
    "Good Night",
    "See you later",
    "How are you",
    "Have a good day",
]

with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

with open("some.txt") as f:  # ファイルを再度開く
    c = 0
    for line in f:  # 変数名 "1" を "line" に修正
        print(line, end="")
        if c == 2:
            break
        c += 1
