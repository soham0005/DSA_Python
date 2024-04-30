def maxSum(arr):
    maxCount = []
    
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(0,rows):
        sumRow = 0
        for j in range(0,cols):
            sumRow = sumRow + arr[i][j]
        maxCount.append(sumRow)
    return max(maxCount)

print(maxSum([[1,2,3],[3,2,1]]))