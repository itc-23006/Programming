import random

# numbersリストを特定の要素で生成
numbers = ["apple", "banana", "cherry", "date"]
num4 = "".join(random.sample(numbers, k=4))

while True:
    va1 = input()
    if va1 == num4:
        break
    if len(va1) != 4:
        print("Input 4 items.")
        continue

    answer = ""
    for i in range(4):
        if num4[i] == va1[i]:
            answer += num4[i]
        else:
            answer += "X"

    print("-> " + answer)
