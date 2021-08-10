def sqrt(a):
    for i in range(a[0],a[1]):
        ans = i ** (1/2)
        if (ans%1==0):
            return int(ans)
        else:
            i += 1
            
print(sqrt([12,32]))
        