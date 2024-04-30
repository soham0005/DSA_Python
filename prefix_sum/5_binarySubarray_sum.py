from collections import Counter
def binarySubArraySum(nums,goal):
    
    res = 0
    prefix_sum = 0
    
    count = Counter({0:1})
    
    for ele in nums:
        prefix_sum += ele
        res += count[prefix_sum-goal]
        count[prefix_sum] +=1
    return res

print(binarySubArraySum([1,0,1,0,1],2))