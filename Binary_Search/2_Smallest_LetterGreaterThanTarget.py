# Question 744 - Leetcode
'''
Approach: Binary Search.
Question Summary:
Return the smallest letter which is greater than the target
ex: for array [1,3,5,6,8,9,10], and target  = 6, the elements which are greater than 6 are 8,9,10 and you need to return the smallest among them that is 8.

And if there is no element grater than target then you need to return the first value at 0th index

'''

def nextGreatestLetter(letters,target):
    start  = 0
    end = len(letters) - 1
    
    while start <= end:
        mid = (start + (end - start) // 2)
        
        if letters[mid] > target:
            end  =  mid - 1
        else:
            start  = mid + 1
    return letters[start % len(letters)]

print(nextGreatestLetter(["c","f","j"],"a"))
 