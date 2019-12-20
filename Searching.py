<<<<<<< HEAD
import math


=======
>>>>>>> 051a0033ac31e83c7c90888f5e4f2d9af2e845e7
def linear(li: object, value: object) -> object:
    for i in range(0, len(li)):
        if li[i] == value:
            print("Position: ", i)
            return
    print("Element doesn't exist")


<<<<<<< HEAD
def binary(li, v, b, e):
    while b <= e:
        n = math.floor(b + (e - b) / 2)
        if li[n] == v:
            return n
        elif v < li[n]:
            e = n
        elif v > li[n]:
            b = n + 1
    return -1


l = [1, 2, 4, 6, 8, 25, 27, 72, 230, 234, 790, 4094, 8645, 35456, 56897, 79236]
v = 790
s = binary(l, v, 0, len(l) - 1)
print("Position: ", s)
=======
l = [77, 26, 84, 26, 84, 25, 25, 7, 23, 23, 7, 4, 86, 35]
v = 7
linear(l, v)
>>>>>>> 051a0033ac31e83c7c90888f5e4f2d9af2e845e7
