def call():
    print('Avengers! Assemble!')


def buy(fruit):
    print('He bought {}'.format(fruit))


def greeting(fisrt_name, last_name):
    print('My name is {} {}'.format(fisrt_name, last_name))


def find_youngest(*kids):
    print('The youngest kid is {}'.format(kids[1]))


def find_youngest_v2(first_kid, second_kid, third_kid):
    print('The youngest kid is {}'.format(third_kid))


def find_kid(**kid):
    print('He is {}'.format(kid['last_name']))


def get_country(country='Viet Nam'):
    print('I\'m from {}'.format(country))


def get_square(num):
    return num * num


def tri_recursion(num):
    if num > 0:
        result = num + tri_recursion(num-1)
        print(result)
    else:
        result = 0
    return result


call()
buy('banana')
buy('apple')
buy('dick')
greeting('Barry', 'Allen')
find_youngest('Barry', 'Wally', 'Bart')
find_youngest_v2(first_kid='Barry', second_kid='Bart', third_kid='Wally')
find_kid(first_name='Barry', last_name='Allen')
get_country('New Zealean')
get_country()
print(get_square(3))
tri_recursion(3)
