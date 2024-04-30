

def longest_subarray_with_sum_k(nums,k):
    
    l = r = 0
    sum = 0
    maxLen = 0
    
    while r < len(nums):
        sum += nums[r]   
        
        while sum > k:
            sum = sum - nums[l]
            l+=1
        
        
        if sum == k:
            maxLen = max(maxLen,r-l+1)
        
        r = r + 1
    return maxLen

print(longest_subarray_with_sum_k([ 1, 2, 1, 0, 1],4))

