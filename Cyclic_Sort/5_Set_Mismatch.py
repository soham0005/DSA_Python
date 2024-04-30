# Leetcode - 645

def Set_Mismatch(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        
        if nums[i] != nums[correct_index]:
            [nums[i],nums[correct_index]] = [nums[correct_index],nums[i]]
        else:
            i = i+1
            
    for index in range(len(nums)):
        if nums[index] != index+1:
            return [nums[index],index+1]
    return [-1,-1]

print(Set_Mismatch([1,2,2,4]))