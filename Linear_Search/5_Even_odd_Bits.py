n = 16
even = 0
odd = 0
print(bin(n)[2:])
binaryAns = bin(n)[2:]
binaryAns = binaryAns[::-1]
for i in range(0,len(binaryAns)):
    # print(binaryAns[i])
    if i % 2 == 0 and binaryAns[i] == '1':
        even += 1
        # print(binaryAns[i])
    elif i % 2 != 0 and binaryAns[i] == '1':
        odd += 1
print(even,odd)