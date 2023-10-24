# Return the Number 

def ceilingNumber(nums,target):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + (end - start) // 2)
        
        if target > nums[mid]:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return start

print(ceilingNumber([1,2,3,4,5,6,10,23,59],7))
