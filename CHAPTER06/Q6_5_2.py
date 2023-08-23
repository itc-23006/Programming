import my_math


def my_pow(x, y):
    return x**y


# my_math2.py
with open("my_math.py", "w") as f:
    f.write(
        """def my_pow(x, y):
    return x ** y\n"""
    )


if __name__ == "__main__":
    x, y, exp = 2, 5, 32
    ans = my_math.my_pow(x, y)
    print("Test my_pow({}, {}) -> {}, exp: {} ---- ".format(x, y, ans, exp), end="")
    if ans == exp:
        print("Test OK")
    else:
        print("Test Fail")
