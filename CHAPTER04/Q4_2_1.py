def number_to_day(num=0):
    if num == 0:
        day = "水曜日"
    elif num == 1:
        day = "木曜日"
    elif num == -1:
        day = "火曜日"
    elif num == 2:
        day = "金曜日"
    elif num == -2:
        day = "月曜日"
    elif num == 3:
        day = "土曜日"
    elif num == 4:
        day = "日曜日"
    else:
        day = "先週"
    return day


print(number_to_day())
print(number_to_day(1))
print(number_to_day(-1))
print(number_to_day(-2))
print(number_to_day(2))
print(number_to_day(3))
print(number_to_day(4))
