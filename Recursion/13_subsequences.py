
def subsequences(ans,string):
    if(len(string) == 0):
        print(ans)
        return
    
    subsequences(ans,string[1:])
    subsequences(ans + string[0],string[1:])
    
subsequences("","abc")
