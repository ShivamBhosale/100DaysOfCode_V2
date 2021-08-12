def uniqueint(arr):
    unique_arr = 0
    for i in arr:
        print('This is the current id begin check',i)
        print('This is the current unique id',unique_arr)
        print('This is the reult of XOR',unique_arr^i,"\n")
        
        unique_arr ^= i
    return unique_arr
    
print(uniqueint([1,2,3,2,1]))