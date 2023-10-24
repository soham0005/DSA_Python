# def reverseList(A,start,end):
#     if start >= end:
#         return
#     A[start], A[end] = A[end], A[start]
#     reverseList(A, start+1, end-1)
    
# A = [1,2,3,4,5]
# print(reverseList(A,0,4))
# print(A)

def reverseList(arr,left,right):
    if left >= right:
        return arr

    arr[left], arr[right] = arr[right], arr[left]
    return reverseList(arr, left + 1, right - 1)

    
ans = reverseList([1,2,3,4,5],0,4)
print(ans)