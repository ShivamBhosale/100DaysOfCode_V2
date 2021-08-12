def removeDuplicate(s):
    result = []
    seen = set()
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

print(removeDuplicate("aabbcc"))

def removeDuplicate2(st):
    result2 = []
    seen2 = set()
    for char2 in st:
        if char2 not in seen2:
            seen2.add(char2)
            result2.append(char2)
    return ''.join(result2)

print(removeDuplicate2("aabbcc dd"))