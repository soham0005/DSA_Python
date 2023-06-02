# Question 75 Leetcode

#Variation of Dutch National Flag
'''
Dutch National Flag uses three pointers low,high,mid
Initially, it is assumed that there are all 0 between low - 1, high+1 to N are 2

The conditions are:
initially low and mid are pointing to 0th Index

Loop:
    if mid is pointing to 0:
        swap values of low and mid and increment low mid
    if mid is pointing to 1:
        increment mid
    if mid is pointing to 2:
        swap values of high and mid and decrement high
        
Time Complexity: O(N)
Spacce Complexity: O(1)

'''


def sortColor(nums):
    high = len(nums) - 1
    low = mid = 0
    
    while mid <=high:
        if  nums[mid] == 0:
            [nums[low],nums[mid]] = [nums[mid],nums[low]]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            [nums[mid],nums[high]] = [nums[high],nums[mid]]
            high -= 1
    print(nums)
    
    
sortColor([2,0,2,1,1,0])