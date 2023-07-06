answer = ""
for i in range(4):
    for j in range(4):
        if i == j:
            answer += "￮"
        else:
            answer += "･"
    answer += "\n"
print(answer)
