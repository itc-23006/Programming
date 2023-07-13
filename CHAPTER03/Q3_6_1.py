import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sample4 = random.sample(numbers, k=4)
num4 = "".join(sample4)

while True:
    va1 = "".join(random.sample(numbers, k=4))
    print(va1)
    if va1 == num4:
        print("OK")
        break
    else:
        print("NG")
