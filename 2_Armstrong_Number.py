# Split the number and cube the individual numbers and add them to generate the armstrong number.

def armStrongNumber(num):
    original = num
    sum = 0
    while num > 0:
        rem =  num % 10
        num =   num // 10
        sum = sum +(rem * rem * rem)
    return sum == original
    
for i in range(100,1000):
    if(armStrongNumber(i)):
        print(i)
        
# print(armStrongNumber(153))