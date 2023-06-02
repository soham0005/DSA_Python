# Leetcode Question 287

#Brute Force Approach

def findDuplicate(nums):
    map = {}
    for ele in nums:
        if ele in map:
            return ele
        map[ele] = 1
    return "No Duplicate Number"

print(findDuplicate([1,3,4,29,2]))