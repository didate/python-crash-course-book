filename = "programming.txt"
with open(filename, 'w') as the_object:
    the_object.write("I Love programming.\n")
    the_object.write("I Love greating new game.\n")

with open(filename, 'a') as the_file:
    the_file.write("I also love finding meaning in large datasets.\n")
    the_file.write("I love creating apps that can run in a browser.\n")
