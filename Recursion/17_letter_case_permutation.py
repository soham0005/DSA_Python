
def letter_case_permutations(s, current, result):
    if len(s) == 0:
        result.append(current)
        return result
    
    if s[0].isdigit():
        letter_case_permutations(s[1:], current + s[0], result)
    else:
        letter_case_permutations(s[1:], current + s[0].lower(), result)
        
        letter_case_permutations(s[1:], current + s[0].upper(), result)
    return result
    
result = []
print(letter_case_permutations("3z4","",result))