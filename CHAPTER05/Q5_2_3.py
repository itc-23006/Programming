print("x", "y", "x*y", sep="\t")  # Print the header

for x in range(3):
    for y in range(x + 1):
        print(x, y, x * y, sep="\t")
