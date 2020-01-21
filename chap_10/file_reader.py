with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


filename = 'pi_digits.txt'
with open(filename) as file:
    for line in file:
        print(line)

# remove blank line
with open(filename) as file:
    for line in file:
        print(line.rstrip())

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())
