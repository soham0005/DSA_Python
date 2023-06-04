# Intersection of Two Sorted Array - Interview Bit

def intersectionArray(A,B):
    ans = []
    
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i+=1
        elif A[i] > B[j]:
            j+=1
        else:
            ans.append(A[i])
            i+=1
            j+=1
    return ans

print(intersectionArray([1,2,3,3,4,5],[3,3,5]))