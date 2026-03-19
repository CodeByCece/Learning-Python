#5-11 Ordinal Numbers

list = []

for i in range(1, 10):
    list.append(i)
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
