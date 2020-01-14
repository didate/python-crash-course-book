motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('Mercedes')
print(motorcycles)

motorcycles.insert(0, 'Mazda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

popped_motorcyle = motorcycles.pop(1)
print(popped_motorcyle)

motorcycles.remove('ducati')
print(motorcycles)
