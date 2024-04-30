# Binary Search for Array sorted in decreasing order

def ReversebinarySearch(nums,target):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + (end - start) // 2)
        
        if target > nums[mid]:
            end = mid - 1
        elif nums[mid] > target:
            start = mid + 1
            
        else:
            return mid
    return False

print(ReversebinarySearch([59,31,20,19,15,10,7,3,1],19))