def string_rev(name):
    if len(name) == 0:
        return name
    else:
        """ return reverse string """
        return string_rev(name[1:]) + name[0]
print(string_rev("cat"))


