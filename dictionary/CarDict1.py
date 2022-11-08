car = {
    'brand' : 'Ford',
    'model': 'Focus',
    'colour' : 'red',
    'year' : 1964,
    'isNew' : False    
}

car.pop('model')

for key, value in car.items():
    print(key, ':', value)