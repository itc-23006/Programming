for e in filter(lambda i: i % 2 == 0, range(1, 11)):
    print(e, end="")  # Output: 246810

pairs = [(2, "down"), (1, "up"), (4, "right"), (3, "left")]
pairs.sort(key=lambda x: x[1])
print(pairs)
