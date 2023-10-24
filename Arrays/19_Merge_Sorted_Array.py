'''

'''

def mergeSortedArray(nums1,nums2):
    i = 0
    j = 0
    
    mergedArray = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] >= nums2[j]:
            mergedArray.append(nums2[j])
            j += 1 
        else:
            mergedArray.append(nums1[i])
            i += 1 
    
    while i < len(nums1):
        mergedArray.append(nums1[i])
        i += 1
    while j < len(nums2):
        mergedArray.append(nums2[j])
        j += 1
    return mergedArray

print(mergeSortedArray([1,3,5,7,9],[2,4,6]))