class sparrow:  # sparrowは雀（すずめ）です。
    cry = "ピヨピヨ"
    legs = 2
    is_animal = True


tama = sparrow()
formatted_string = "鳴き声: {}, 足の数: {}, 動物: {}".format(
    tama.cry, tama.legs, tama.is_animal
)
print(formatted_string)
