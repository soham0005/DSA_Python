def primeOrNot(num):
    if num <= 1:
        return False
    c =2
    while c * c <= num:
        if num % c == 0:
            return False
        c +=1
    if num <= c*c:
        return True
    return False
        
print(primeOrNot(3))