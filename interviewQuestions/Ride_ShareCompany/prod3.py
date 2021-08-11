def solution(lst):
    high = max(lst[0],lst[1])
    low = min(lst[0],lst[1])
    
    high_prod2 = lst[0] * lst[1]
    low_prod2 = lst[0] * lst[1]
    
    high_prod3 = lst[0] * lst[1] * lst[2]
    
    for num in lst[2:]:
        high_prod3 = max(high_prod3, high_prod2 * num, low_prod2 * num)
        high_prod2 = max(high_prod2,num * high,num * low)
        
        low_prod2 = min(low_prod2,num * high,num * low)
        
        high = max(high,num)
        low = min(low,num)
        
    return high_prod3
print(solution([99,-82,82,40,75,-24,39, -82, 5, 30, -25, -94, 93, -23, 48, 50, 49,-81,41,63]))