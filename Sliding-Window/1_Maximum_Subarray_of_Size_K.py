
def maximum_sum_subarray(nums,k):
    
    if k <= 0  or  k < len(nums):
        return 0
    
    left = right = 0
    
    max_sum = float("-inf")
    curr_sum = 0
    
    
    while right < len(nums):
        curr_sum += nums[right]
        
        
        if right - left + 1 == k:
            max_sum = max(max_sum,curr_sum)
            curr_sum -= nums[left]
            left+=1
        right+=1
        
    return max_sum

print(maximum_sum_subarray([]))