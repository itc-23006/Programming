def fib(n):
    """n以下のフィボナッチ数列を列挙する"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


# 実行例 #print()を書かなくても出力できた。
print(fib(1000))
