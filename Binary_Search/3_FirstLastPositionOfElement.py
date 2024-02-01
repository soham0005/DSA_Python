# First and Last Position of Element in an Array - Leetcode Q.34
'''
Approach: Use Binary Search twice one for First Position and one for Last Position

'''
def firstOccurence(nums,target):
    start = 0
    end = len(nums) - 1
    occ = -1
    
    while start <= end:
        mid  = (start + (end - start) // 2)
        
        if nums[mid] == target:
            occ = mid
            end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return occ

def lastOccurence(nums,target):
    start = 0
    end = len(nums) - 1
    occ = -1
    
    while start <= end:
        mid  = (start + (end - start) // 2)
        
        if nums[mid] == target:
            occ = mid
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return occ
print(lastOccurence([5,7,7,7,7,7,7,8,8,10],7))
print(firstOccurence([5,7,7,7,7,7,7,8,8,10],7))



            