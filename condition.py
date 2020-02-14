a = 33
b = 200
if b > a:
    print('b > a')


a = 1
b = 1
if a > b:
    print('a > b')
elif a == b:
    print('a = b')

a = 200
b = 33
if b > a:
    print('b > a')
elif a == b:
    print('a = b')
else:
    print('a > b')

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

x = 41
if x > 10:
    print('Above 10')
    if x > 20:
        print('And also above 20')
    else:
        print('But not above 20')
