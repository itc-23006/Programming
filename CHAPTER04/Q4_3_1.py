def concat_words(*args, separator="."):
    return separator.join(args)


# 実行
print(concat_words("a", "b", "c", "d", separator="_"))

print(concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator=" "))
print(concat_words("沖縄県", "那覇市", "樋川", "一丁目", "3-41", separator=""))
