# Merge Sorted Array withou Extra space - LeetCode Q.88

def merge(nums1,nums2,m,n):
    i = m - 1
    j = n - 1
    index = m + n -1
    
    while i >=0 and j >=0:
        if nums1[i] > nums2[j]:
            nums1[index] = nums1[i]
            i -= 1
            index -=1
        elif nums2[j] > nums1[i]:
            nums1[index] = nums2[j]
            j -= 1
            index -=1
        else:
            nums1[index] = nums1[i]
            nums1[index-1] = nums2[j]
            index -=2
            j-=1
            i-=1
    while j>=0:
        nums1[index] = nums2[j]
        j-=1
        index-=1
    return nums1

print(merge([1,2,3,0,0,0],[2,5,6],3,3))