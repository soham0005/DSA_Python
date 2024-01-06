# Find Duplicate Number - Leetcode - 287
'''
Approach: Use Cyclic Sort and add one condition that if element is not in its correct position then check once again if at correct index if the element is present or not; if present then return the number


'''

def find_Duplicate_Number(nums):
    i = 0
    
    while i < len(nums):
        if nums[i] !=  i+1:
            correct = nums[i] - 1
            
            if(nums[i] != nums[correct]):
                [nums[i],nums[correct]] = [nums[correct],nums[i]]
            else:
                return nums[i]
        else:
            i = i + 1
    return -1


print(find_Duplicate_Number([1,3,4,2,2]))
            