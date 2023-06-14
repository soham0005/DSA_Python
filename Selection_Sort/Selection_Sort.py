'''
Approach: Set the first element as the smallest element just for now;
in loop, check if the next element is smaller than smallest element if smallest, assign smallest to next
Continue till the end, at the end; swap the smallest with a counter which is pointing to 0 and increment the pointer
'''

def Selection_Sort(nums):
    for counter in range(len(nums)):
        minIndex = counter
        for i in range(counter+1,len(nums)):
            if nums[i] < nums[minIndex]:
                minIndex = i 
                
        [nums[minIndex],nums[counter]] = [nums[counter],nums[minIndex]]
        
    return nums 
print(Selection_Sort([1,3,2,5,7,12,9,211,20]))
    