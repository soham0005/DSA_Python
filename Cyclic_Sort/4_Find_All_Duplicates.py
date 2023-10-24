# Leetcode - 442 Find All Duplicates in the Array
'''
Approach: Find Duplicates and store in array
'''

def find_all_duplicates(nums):
    i = 0
    duplicates = []
    
    while i < len(nums):
        correct = nums[i] - 1
        
        if nums[i] != nums[correct]:
            [nums[i],nums[correct]] = [nums[correct],nums[i]]
        else:
            i = i + 1
            
    for index in range(len(nums)):
        if nums[index] != index + 1:
            duplicates.append(nums[index])
    return duplicates
    
print(find_all_duplicates([4,3,2,7,8,2,3,1]))