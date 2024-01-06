# Find Element in Mountain array - Leetcode 1095

''''
Approach :- Find Peak Element
Apply Binary Search in First Half form 0 to peak Index
If element not found then apply binary search in second Half which is in decreasing order.

'''
def ReversebinarySearch(nums,target,mystart,myend):
    start = mystart
    end = myend
    
    while start <= end:
        mid = (start + (end - start) // 2)
        
        if target > nums[mid]:
            end = mid - 1
        elif nums[mid] > target:
            start = mid + 1
            
        else:
            return mid
    return -1

def binarySearch(nums,target,mystart,myend):
    start = mystart
    end = myend
    
    while start <= end:
        mid = (start + (end - start) // 2)
        
        if target > nums[mid]:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

def peakElementIndex(nums):
    start = 0
    end = len(nums) - 1
    
    while start < end:
        mid = (start + (end - start) // 2)
        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid + 1
    return start

# print(peakElementIndex([1,2,3,4,5,2,1]))


def findInMountainArray(target,mountain_arr):
    peakIndex = peakElementIndex(mountain_arr)
    ans = binarySearch(mountain_arr,target,0,peakIndex)
    
    if(ans != -1):
        return ans        
    else:
        ans = ReversebinarySearch(mountain_arr,target,peakIndex,len(mountain_arr)-1)
           
    return ans
    
    
    
    
print(findInMountainArray(3,[0,1,2,4,2,1]))