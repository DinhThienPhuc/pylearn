def myFunc(n):
    return lambda a: a + n


my_doubler = myFunc(1)
print(my_doubler(6))
