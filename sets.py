thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

print('apple' in thisset)

thisset.add('meomeo')
print(thisset)

thisset.update(['melodymark', 'eimi'])
print(thisset)

print(len(thisset))

# Use discard will not raise error but remove. Consider to when using them
thisset.discard('eimi')
print(thisset)
