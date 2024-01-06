
def firstUpperCase(string):
    if(len(string) == 0):
        return -1
    
    if (string[0].isupper()):
        return string[0]
    
    return firstUpperCase(string[1:])
    
print(firstUpperCase("gees"))

    