
def skipString(string):
   
    if(len(string) == 0):
        return ""
    
    if(string.startswith("apple")):
        return skipString(string[5:])
    else:
        return string[0] +  skipString(string[1:])
    
print(skipString("helloappleasdas"))