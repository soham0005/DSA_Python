# Leetcode 136

def missingNumber(arr):
    ans = 0
    for ele in arr:
        ans = ans ^ ele
    return ans


# print(missingNumber([1,2,1,3,3,4,4]))
print(
    
)