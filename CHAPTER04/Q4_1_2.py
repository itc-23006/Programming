def fib(n):
    """nより小さなフィボナッチ数列をリストで返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# 実行例 # printを入れないと出力できない。
# 理由としては、問題1と違ってprint()が宣言されてないから。
print(fib(1000))
