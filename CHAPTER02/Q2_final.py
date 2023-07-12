import random

name = "OshiroAoi"

while True:
    random_letter = chr(random.randint(65, 90))

    print(random_letter)

    if random_letter == name[0]:
        break
