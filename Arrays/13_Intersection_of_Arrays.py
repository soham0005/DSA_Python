#Intersection of two Arrays - Leetcode.


def intersection(nums1,nums2):
    ans = set()
    for i in nums1:
        if i in nums2:
            ans.add(i)
    print(list(ans))
    
# One Liner Solution -   return list(set(nums1) & set(nums2))
    
    
intersection([1,2,2,1],[2,2])