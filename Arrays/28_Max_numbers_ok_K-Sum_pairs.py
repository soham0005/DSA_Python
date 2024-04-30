def maxOperations(nums,k):
    i,j = 0,len(nums)-1
    count = 0
    
    while i < j:
        if nums[i] + nums[j] == k:
            count+=1
            i+=1
            j-=1
        elif nums[i] + nums[j] > k:
            j-=1
        else:
            i+=1
    return count
            
            



nums = [3,1,3,4,3] 

print(maxOperations(nums,6))