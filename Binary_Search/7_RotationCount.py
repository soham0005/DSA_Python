# Find how many times the Sorted Array is Rotated
'''
Approach:- Find the Pivot Index and return Pivot + 1
[4,5,6,7,0,1,2]
'''

def findPivotIndex(nums):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + (end - start) //2 )
        
        if mid < end and nums[mid] > nums[mid+1]:
            return mid
        elif mid<end and nums[mid] < nums[mid-1]:
            return mid - 1
        elif nums[start] > nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    

def findRotationCount(nums):
    return findPivotIndex(nums) + 1


print(findRotationCount([6,7,8,9,1,2,3,4,5]))