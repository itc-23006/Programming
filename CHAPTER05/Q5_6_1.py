a = {x for x in "abcabcabc" if x not in "c"}
b = {y for y in "abcabcabc" if y not in "c"}
result = a | b
print(result)
