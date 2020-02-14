lst = ["apple", "banana", "cherry"]
print(lst)
print(lst[1])
print(lst[-3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])

print('-------')
print(thislist[-4:-1])

thislist[1] = "blackcurrant"
print(thislist)

print('mmmmmmm')
for x in thislist:
    print('item {}'.format(x))

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print(len(thislist))

thislist.append('ahihi do cho')
print(thislist)

thislist.insert(2, 'cacacacacca')
print(thislist)

thislist.remove('orange')
print(thislist)

del thislist[1]
print('vvvvvvvvvvvv')
print(thislist)

thislist.clear()
print(thislist)

thislist.append('ahihi')
thislist.append('docho')
print(thislist)

newList = thislist.copy()
print(newList)

newnewList = list(thislist)
print('----- {}'.format(newList))

list3 = newList + newnewList
list4 = ['asdada', 'iiiii']
list4.extend(newnewList)
print(list3)
print(list4)
