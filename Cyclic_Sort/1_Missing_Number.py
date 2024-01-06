# Leetcode - 268 Missing Number
'''
Approach: Use Cyclic Sort as Range is given in the question.

Use Cyclic Sort to Sort the Array and Run a loop and return the index which is not equal to the element
In Case, You dont find the Index which does not match then the N is your Answer
'''

def MissingNumber(nums):
    i = 0
    
    while i < len(nums):
        correct_index = nums[i]
        
        if nums[i] < len(nums) and nums[i] != nums[correct_index]:
            [nums[i],nums[correct_index]] = [nums[correct_index],nums[i]]
        else:
            i = i+1
            
    for index in range(len(nums)):
        if nums[index] != index:
            return index
    return len(nums)

print(MissingNumber([9,6,4,2,3,5,7,0,1]))