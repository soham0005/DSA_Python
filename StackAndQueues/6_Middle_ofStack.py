def deleteMid(s, sizeOfStack):
    if (sizeOfStack % 2  == 0):
        mid = int((sizeOfStack //2) - 1)
        del s[mid]
    else:
        mid = int(sizeOfStack // 2)
        del s[mid]
        