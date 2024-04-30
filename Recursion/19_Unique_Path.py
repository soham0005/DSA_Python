def unique_path(m,n):
    if m == 1 or n == 1:
        return 1
    
    left = unique_path(m-1,n)
    right = unique_path(m,n-1)
    
    return left + right

print(unique_path(3,7))