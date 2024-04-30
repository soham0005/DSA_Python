# LeetCode Question - 283

'''
Approach:- assign j to the first zero in the array.
Loop i from j+1 to end and swap with the j if i is zero and increment j
Time Complexity: O(x) - for finding first zero in array, O(n-x) for swapping 
Final Complexity is O(n)
Space Complexity - O(1)

'''

def moveZeroes(nums):
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
        
    if j!= -1:
        for i in range(j+1,len(nums)):
            if nums[i] != 0:
                [nums[i],nums[j]] = [nums[j],nums[i]]
                j += 1
    print(nums)
    
# moveZeroes([0,1,0,3,12])
print(7 % 10)