def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func


def add(x, y):
    return x + y


result = add(3, 5)
print("Result:", result)
