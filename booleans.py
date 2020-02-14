print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 19
b = 1
if a > b:
    print('a is greater than b')
else:
    print('a is not greater than b')

print(bool(10))
print(bool(''))
print(bool('aosjd'))


print(bool(["apple", "cherry", "banana"]))


class myClass():
    def __len__(self):
        return 0


myObj = myClass()
print('------')
print(bool(myObj))


def myFunction():
    return True


print('test func')
print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")
