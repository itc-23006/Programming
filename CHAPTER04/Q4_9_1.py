def spam(ham, eggs):
    print(eggs)


foo = (0,)
spam(foo[0], {"eggs": 2})  # spam関数を呼び出し

x = 4
y = 2
if x == 4:
    print(x, y)
    x, y = y, x

print(x, y)
