# Union of two sorted array - GFG Question

'''
Brute Force Approach: Take a set and add the elements and sort the set.

Optimum Approach:- Use two pointer and push the smallest element among the pointer into the new union array which is to be returned.



'''

def findUnion(a,b,n,m):
    i = 0
    j = 0
    unionArray = []
    
    while i<n and j <m:
        if a[i] <= b[j]:
            if len(unionArray) == 0 or a[i] != unionArray[-1]:
                unionArray.append(a[i])
            i+=1
        else:
            if len(unionArray) == 0 or b[j] != unionArray[-1]:
                unionArray.append(b[j])
            j += 1
        
    while j<m:
        if len(unionArray) == 0 or b[j] != unionArray[-1]:
                unionArray.append(b[j])
        j += 1
        
    while i<n:
        if len(unionArray) == 0 or a[i] != unionArray[-1]:
                unionArray.append(a[i])
        i += 1
        
    return unionArray

print(findUnion([1,2,3,4,5],[1,2,3],5,3))         
        