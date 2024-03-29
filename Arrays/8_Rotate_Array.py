# Leetcode Question - 189 Right Rotate Array by "k" steps.

'''
Approach: 
Reverse Array 
then split into blocks 
Reverse the Block and join

'''

def RotateArray(nums,k):
    
    k = k % len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums
    

print(RotateArray([-1,-100,3,99],2))