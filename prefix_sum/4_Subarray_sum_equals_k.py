def subArraySum(nums,k):
    res = 0
    map = {0:1}
    prefix_sum = 0
    
    
    for ele in nums:
        
        prefix_sum += ele
        
        if prefix_sum - k in map:
            res += map[prefix_sum - k]
        
        if prefix_sum not in map:
            map[prefix_sum] = 1
        else:
            map[prefix_sum] +=1
    return res
        
            
print(subArraySum([1,1,1],2))