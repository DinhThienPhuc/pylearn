# Comment
"""
New comment
"""
print('hello world')
x, y, z = 5, 2, 'Fuck'
if x > y:
    print('Five is greater than two ' + z)

a = 'shitty'


def myFunc():
    a = 'good'
    print('Python is ' + a)


myFunc()
print('Python is ' + a)


def newFunc():
    global m
    m = 'ahihi'
    print('Test ------ ' + m)


newFunc()

print('Test ------ ' + m)
