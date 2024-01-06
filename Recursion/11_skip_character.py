def skipACharacter(string):
    
    if(len(string) == 0):
        return ""

    if(string[0] == "a"):
        return skipACharacter(string[1:])
    else:
        return string[0] + skipACharacter(string[1:])
        
        
print(skipACharacter("abccdah"))