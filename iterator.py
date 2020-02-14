fruits = ("apple", "banana", "cherry")
iterator_point = iter(fruits)

print(next(iterator_point))
print(next(iterator_point))
# print(next(iterator_point))

fruit = "banana"
char_iter = iter(fruit)

print(next(char_iter))
print(next(char_iter))
print(next(char_iter))
print(next(char_iter))

for fruit in fruits:
    print('shit {}'.format(fruit))
