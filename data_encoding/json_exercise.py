import json

## reads key id values on separate lines. 
# with open('C:/vscode/Python/Exercises/data_encoding/example.json') as file:
#     data = json.load(file)

# for item in data['menu']['items']:
#     print(item['id'])

data = {
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}

with open('output.json', 'w+') as file:
    json.dump(data, file)

with open('output.json') as file1:
    data1 = json.load(file1)
print(data)