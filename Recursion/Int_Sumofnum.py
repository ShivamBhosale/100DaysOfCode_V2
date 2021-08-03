def sumOfNumbers(n):
    if n <= 1:
        return n
    else:
        return n + sumOfNumbers(n-1)
    
print(sumOfNumbers(10))