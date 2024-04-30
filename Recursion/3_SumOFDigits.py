def sum(n):
    if n == 0:
        return 0
    return (n%10) + sum(n//10)


def product(n):
    if n%10 == n:
        return n
    return (n%10) * product(n//10)
print(sum(11))
print(product(1342))