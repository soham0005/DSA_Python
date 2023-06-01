def searchInString(word,target):
    for i in range(len(word)):
        if word[i] == target:
                    return i
    return False

print(searchInString("soham","a"))