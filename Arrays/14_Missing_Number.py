# Find the missing number - GFG

'''
Brute Force Approach :- Use Linear Search in Loop to search individual element
TC: O(n^2)

Better Approach:- Use Hashmap

Optimal Approach:- There are 2 optimal solutions for this problem, one is using sum and second is using xor

Sum Approach:- To get the missing number, result of sum of n natural numbers (n * n+1)/2  -  sum of array elements is the missing number 

Second approach is by using xor operation


'''


def missingNumber(arr,n):
    sumOfN = (n * (n+1)) // 2
    return sumOfN -  sum(arr)

    
print(missingNumber([1,2,4,5],5))