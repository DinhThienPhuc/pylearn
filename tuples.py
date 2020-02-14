thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(thistuple[2])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])

meo = list(thistuple)
meo[0] = 'shitty'
thistuple = tuple(meo)
print(thistuple)

for x in thistuple:
    print('--- {}'.format(x))

if "kiwi" in thistuple:
    print('Yes, \'kiwi\' is in the fruits tuple')

print(len(thistuple))

x = ("apple",)
print(type(x))

# NOT a tuple
x = ("apple")
print(type(x))

# del x
# print(x)

thistuple = tuple(("apple", "banana", "cherry", 'ahjihih'))
print(thistuple)
