
# Parameterized way
# def sumOfNumbers(i,sum):
#     if i<1:
#         print(sum)
#         return
#     sumOfNumbers(i-1,sum+i)
    
# sumOfNumbers(5,0)

# Functional Way
def sumOfNumber(i,n,sum):
    # if n==0:
    #     return 0
    # return n + sumOfNumber(n-1)
    if i == n:
        print(sum+i)
        return
    sumOfNumber(i+1,n,sum+i)

print(sumOfNumber(1,3,0))