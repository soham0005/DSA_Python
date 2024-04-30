arr = [1,3,2]
res = []
n = len(arr)
for i in range(len(arr)-1):
    minEle = min(arr[i+1:])
    print(minEle)
    print(arr[i+1:])
    if arr[i] > minEle:
        res.append(minEle)
    else:
        res.append(-1)
res.append(-1)
    
print(res)
    
