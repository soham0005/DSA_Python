# gfg check if Kth Bit is set or not


def setOrNot(n,k):
    mask = 1 << k
    flag =  mask & n
    return flag

# print(setOrNot(4,2))
# print(3 ^ 2)