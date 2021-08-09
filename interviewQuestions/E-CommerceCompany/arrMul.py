def arrMul(lst):
    out = [None] * len(lst)
    prod = 1
    i = 0 
    while i < len(lst):
        out [i] = prod
        prod *= lst[i]
        
        i += 1
        
    prod = 1
    i = len(lst) - 1
    
    while i >= 0:
        out[i] *= prod
        prod *= lst[i]
        i -= 1 
    return out

print(arrMul([1,2,3,4]))
   
    
    