import json

person_str = '{ "name":"Barry", "age":35, "city":"Central City"}'

person_dict = json.loads(person_str)

print(person_dict['name'])

car = {
    'name': 'chervolet',
    'year': 1977
}

car_str = json.dumps(car)
print(car_str)

mix = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}

print(json.dumps(mix))
