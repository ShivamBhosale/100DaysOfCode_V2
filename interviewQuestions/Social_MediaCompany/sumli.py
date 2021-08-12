def solution(lst,tar):
    seen = set()
    for num in lst:
        num2 = tar - num
        if num2 in seen:
            return True
        seen.add(num)
    return False

print(solution([1,2,3,4,5],6))

def solution2(lst2,tar2):
    for i in range(len(lst2)):
        n = tar2 - lst2[i]
        if n in lst2:
            return True
    return False


print(solution2([1,2,3,4,5],11))