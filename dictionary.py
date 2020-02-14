thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

print(thisdict['year'])

thisdict['year'] = 1977
print(thisdict)


for key in thisdict:
    print(key)

for key in thisdict:
    print(thisdict[key])

for val in thisdict.values():
    print(val)

for key, value in thisdict.items():
    print('{}: {}'.format(key, value))

if 'year' in thisdict:
    print('\'year\' is in this dict')

print(len(thisdict))

thisdict['ahihi'] = 'do cho'
print(thisdict)

thisdict.pop('ahihi')
print(thisdict)

del thisdict

thisdict = {
    'name': 'kai',
    'age': 25,
    'gender': 'male'
}
print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
    'name': 'kai',
    'age': 25,
    'gender': 'male'
}

newdict1 = thisdict.copy()
newdict2 = dict(thisdict)
print(newdict1)
print(newdict2)

newdict1['name'] = 'ghoul'
newdict2['gender'] = 'lgbt'
print(thisdict)
print(newdict1)
print(newdict2)

del thisdict
del newdict1
del newdict2

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
