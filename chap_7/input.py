message = input('What is your name : ')

age = input('How old are you ? ')
if 18 <= int(age):
    print(message + ', You are adult')
else:
    print(message + ', You are very younger')
