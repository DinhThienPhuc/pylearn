fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


print('----------------------------------------------------------------------')
for letter in 'Avenger':
    print(letter)


print('----------------------------------------------------------------------')
cars = ['chervolet', 'audi', 'bwm']
for car in cars:
    print(car)
    if car == 'audi':
        break


print('----------------------------------------------------------------------')
gaming_brands = ['razer', 'steelseries', 'logitech']
for gaming_brand in gaming_brands:
    if gaming_brand == 'logitech':
        break
    print(gaming_brand)


print('----------------------------------------------------------------------')
gaming_brands = ['razer', 'steelseries', 'logitech']
for gaming_brand in gaming_brands:
    if gaming_brand == 'razer':
        continue
    print(gaming_brand)


print('----------------------------------------------------------------------')
for num in range(7):
    print(num)


print('----------------------------------------------------------------------')
for num in range(3, 7):
    print(num)


print('----------------------------------------------------------------------')
for num in range(3, 7, 2):
    print(num)


print('----------------------------------------------------------------------')
for num in range(6):
    print(num)
else:
    print('Finally finished!')


print('----------------------------------------------------------------------')
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjs:
    for y in fruits:
        print(x, y)
