# Leetcode - 169 

'''
Brute Force : Return the element which has occurence more than N/2

Optimum Approach: Moore's Voting Algorithm
'''


def majorityElement(nums):
    map = {}
    for ele in nums:
        if ele not in map:
            map[ele] = 1
        else:
            map[ele] +=1
    print(map)
    for key in map:
        if(map[key] > len(nums)/2):
            print(key)
    
# majorityElement([3,3,2])


def majorityElementMooreVoting(nums):
    count = 0
    ele = -1
    for i in range(len(nums)):
        if count == 0:
            ele = nums[i]
            count = 1
        elif ele == nums[i]:
            count+=1
        else:
            count -=1
    counter1 = 0
    for val in range(len(nums)):
        if nums[val] == ele:
            counter1 +=1
    if counter1 > len(nums) // 2:
        return ele
    return -1
    
print(majorityElementMooreVoting([2,2,1,1,2,2]))