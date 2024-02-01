
def subsequences(ans,string):
    if(len(string) == 0):
        print(ans)
        return
    
    subsequences(ans,string[1:])
    subsequences(ans + string[0],string[1:])
    
# subsequences("","abc")


def subsequence(ans,string,output):
    if len(string) == 0:
        output.append(ans)
        return output

    subsequence(ans,string[1:],output)
    subsequence(ans+string[0],string[1:],output)
    
    return output

# print(subsequence("","abc",[]))
ans = subsequence("","abc",[])
print(ans)