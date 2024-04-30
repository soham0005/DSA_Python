dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


def solve(index,digits,path,output):
    if index >= len(digits):
        output.append(path)
        return
    
    string = dic[digits[index]]
    
    for j in string:
        solve(index+1,digits,path+j,output)
    
def letterCombination(digits):
    
    if len(digits) == 0:
        return []
    output = []
    path = ''
    index = 0
    
    solve(index,digits,path,output)
    return output
    


print(letterCombination("23"))



