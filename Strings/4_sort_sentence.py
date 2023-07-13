# leetcode - 1859

def sortSentence(s):
    # s = s.spli
    pass

def sort_key(item):
    return int(item[-1])

s = "is2 sentence4 This1 a3"
s = s.split(" ")
s.sort(key=sort_key)
print(s)