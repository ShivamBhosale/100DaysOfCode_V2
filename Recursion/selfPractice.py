def string_reverse(word):
    if len(word) == 1:
        return word
    else:
        return string_reverse(word[1:]) + word[0]
    
print(string_reverse("hello"))

""" --- """
def palindromCheck(word2):
    if len(word2) == 1 or len(word2) == 0:
        return True
    else:
        return word2[0] == word2[-1] and palindromCheck(word2[1:-1])
print(palindromCheck("mayam"))

""" --- """

def sumOfNum(num):
    if num == 1:
        return 1
    else:
        return num + sumOfNum(num-1)
print(sumOfNum(10))
""" --- """

def fib(n):
    
    if n == 1 or n == 0:
        return n
    else:
        return fib(i-1) + fib(i-2)
        
print(fib(7))