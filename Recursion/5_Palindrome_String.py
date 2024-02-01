def isPalindrome(string,i,n):
    if i>=n // 2:
        return True
    
    if string[i] != string[n-i-1]:
        return False
    
    return isPalindrome(string,i+1,n)

string = "sohammahos"
n = len(string)
print(isPalindrome(string,0,n))