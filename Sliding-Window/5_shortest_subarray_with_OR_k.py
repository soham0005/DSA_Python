
def shortest_subarray_with_OR_k(nums,k):
    
    n = len(nums)
    result = float("-inf")
    prefix_or = 0
    left = 0
    
    for right in range(len(nums)):
        
        prefix_or |= nums[right]
        
        
        while left <= right and prefix_or >= k:
            
            result = min(result,right - left + 1)
            prefix_or &= ~nums[left]
            