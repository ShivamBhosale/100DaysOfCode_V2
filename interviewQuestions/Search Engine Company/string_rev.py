def name(a):
    if len(a) == 0 or len(a) == 1:
        return a
    else:
        return name(a[1:]) + a[0]

print(name('HelloWorld'))