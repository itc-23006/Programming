def list_average(x):
    try:
        return sum(x) / len(x)
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of an empty list")
        return None


print(list_average([3.9, 4.5, 2.3]))
print(list_average([]))
