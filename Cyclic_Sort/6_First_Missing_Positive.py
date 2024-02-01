# Leetcode - 41  First Missing Positive

def First_Missing_Positive(nums):
    i = 0
    
    while i < len(nums):
        correct_index = nums[i] -1
        
        if nums[i] > 0  and nums[i] <= len(nums) and nums[i] != nums[correct_index]:
            [nums[i],nums[correct_index]] = [nums[correct_index],nums[i]]
        else:
            i = i+1
            
    for index in range(len(nums)):
        if nums[index] != index+1:
            return index+1
    return len(nums)+1

print(First_Missing_Positive([1,2,0]))