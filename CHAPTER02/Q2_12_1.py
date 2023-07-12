print(pow(2, 3))

result = 1  # 初期値を１にする。
for _ in range(3):  # for文を使ってループさせる。rangeに数字の3を入れてループする回数を指定する.。
    result *= 2  # 1*2, 2*2, 4*2のように出力されます。
print(result)  # printでresultの結果を出力します。
