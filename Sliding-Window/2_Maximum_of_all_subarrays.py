# 
'''
Approach:
1) use SortedList from sortedcontainers
2) until sortedlist if of size k add elements
3) Once length is k, append the last element(max is stored at last in sortedlist) to ans
4) Remove i-k ele and add i ele

'''
from sortedcontainers import SortedList

def maxEleFromSubArray(arr,n,k):
    ans = []
    sortedEleList = SortedList()
    
    for i in range(n):
        if len(sortedEleList) < k:
            sortedEleList.add(arr[i])
        else:
            ans.append(sortedEleList[-1])
            sortedEleList.discard(arr[i-k])
            sortedEleList.add(arr[i])
    ans.append(sortedEleList[-1])
    
    return ans


print(maxEleFromSubArray([1, 2, 3, 1, 4, 5, 2, 3, 6],9,3))