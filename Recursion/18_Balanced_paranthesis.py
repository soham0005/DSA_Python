
def BalancedParanthesis(n):
    open = n
    close = n
    
    output = []
    path = ""
    
    solve(open,close,path,output)
    return output
    
def solve(open_count, close_count, path, output):
    if open_count == 0 and close_count == 0:
        output.append(path)
        return

    if open_count != 0:
        solve(open_count - 1, close_count, path + "(", output)
    
    if close_count > open_count:
        solve(open_count, close_count - 1, path + ")", output)
        
n = 3
result = BalancedParanthesis(n)
print(result)