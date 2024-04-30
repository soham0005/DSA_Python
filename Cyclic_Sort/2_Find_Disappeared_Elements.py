# Leetcode - 448
'''
Approach: Same as Missing Number
'''

def findDisappearedOne(nums):
    output = []
    i = 0
    
    while i < len(nums):
        correct_index = nums[i] - 1
        
        if nums[i] != nums[correct_index]:
            [nums[i],nums[correct_index]] = [nums[correct_index],nums[i]]
        else:
            i += 1
    for index in range(len(nums)):
        if nums[index] != index+1:
            output.append(index+1)
    return output
print(findDisappearedOne([1,1]))