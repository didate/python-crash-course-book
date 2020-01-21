import json
numbers = [1, 2, 4, 5, 6, 34]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
