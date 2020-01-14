cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('------------------------------')
car = 'audi'
if car in cars:
    print('this car exist in list of cars')

print('------------------------------')

car = 'mercedes'
if car not in cars:
    print('this car doesn\'t exist in list of cars')
print('------------------------------')

age = 30
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $"+str(price)+".")
