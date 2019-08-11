def linear(li: object, value: object) -> object:
    for i in range(0, len(li)):
        if li[i] == value:
            print("Position: ", i)
            return
    print("Element doesn't exist")


l = [77, 26, 84, 26, 84, 25, 25, 7, 23, 23, 7, 4, 86, 35]
v = 7
linear(l, v)
