# GFG Question - Left Rotate An array by D Positions 

'''
Brute Force Solution is to swap the elements by n % d

Optimal is break the array into sections and reverse the chunks and again reverse the whole array.


'''


# [1,2,3,4,5], N = 5, D = 2

def leftRotateArraybyD(A,D):
    A[0:D] = A[0:D][::-1]
    A[D:] = A[D:][::-1]
    A = A[::-1]
    return A

print(leftRotateArraybyD([1,2,3,4,5],2))
    