def make_addfunc():
    def add(x, y):
        return x + y

    return add


# Usage:
add_function = make_addfunc()
result = add_function(1, 10)
print(result)  # Output: 5
