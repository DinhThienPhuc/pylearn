a = 'hello world'
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(b)
print(a[0])
print(a[2:7])  # take from 2 to 7, count from start of string with 0

print(a[-7:-2])  # take from 7 to 3, count from end of string, start with -1

print(len(a))

a = ' hello world  '
print(a.strip())

a = 'HELLO WORLD'
print(a.lower())

a = 'hello world'
print(a.upper())

a = 'meo Meo Meo'
print(a.replace('m', 'h'))

a = "Hello, World!"
print(a.split(', '))

txt = "The rain in Spain stays mainly in the plain"
ainInTxt = 'ain' in txt
print(ainInTxt)

fuckNotInTxt = 'fuck' not in txt
print(fuckNotInTxt)

a = 'Hello'
b = 'World'
c = a + '-' + b
print(c)

age = 35
txt = 'My name is Shitty, and I am {}'
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "She wants {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {1} dollars for {2} pieces of item {0}."
print(myorder.format(itemno, price, quantity))

txt = 'We are the so-called \'Vikings\' from the north.'
print(txt)

a = 'aOPA asdawaaJKAnAILLFJljKFlkhj lkjasD'
print(a.capitalize())

txt = "Hello, And Welcome To My World!"
print(txt.casefold())

txt = 'banana'
print(txt.center(20, '-'))

txt = 'I love apples, apple are my favorite fruit'
