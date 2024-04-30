
"""
Idea is to check prefix_sum + suffix_sum == total Sum
i.e 
"""
def checkIfDivisible(nums):
    total_sum = sum(nums)
    print(total_sum)
    
    prefix_sum = 0
    
    for i in range(len(nums)):
        prefix_sum += nums[i]
        suffix_sum = total_sum - prefix_sum
        
        if prefix_sum == suffix_sum:
            return True
    return False


print(checkIfDivisible([1,5,11,5]))