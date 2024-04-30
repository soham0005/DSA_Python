def first_negative(arr,k):
    from collections import deque
    ans = []
    q = deque()
    
    i,j = 0,0
    n = len(arr)
    
    while j < n:
        
        if arr[j] < 0:
            q.append(arr[j])
            
        if j - i +1 < k:
            j += 1
            
        elif j - i +  1  == k:
            if not q:
                ans.append(0)
            else:
                ans.append(q[0])
            
            if arr[i] < 0:
                q.popleft()
            i+=1
            j+=1
    return ans

# Example usage:
arr = [5, -3, 2, 3, -4]
k = 2
print("First negative number in each window of size", k, ":", first_negative(arr, k))
        