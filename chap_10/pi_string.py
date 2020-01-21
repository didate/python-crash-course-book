filename = 'pi_digits.txt'
with open(filename) as the_file:
    lines = the_file.readlines()
print(lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'
with open(filename) as the_file:
    lines = the_file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52]+"...")
print(len(pi_string))
