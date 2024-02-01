def canMakeProgresssion(arr):
    arr = sorted(arr)
    l = len(arr)
    diff = arr[1] - arr[0]
    for i in range(1,l-1):
        if arr[i+1] - arr[i] != diff:
            return False
    return True
    
print(canMakeProgresssion([3,5,1]))
    