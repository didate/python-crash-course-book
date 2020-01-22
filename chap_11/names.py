from name_function import get_formated_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if first == 'q':
        break
    formated_name = get_formated_name(first, last)
    print("\nNeatly fomatted name: " + formated_name + ".")
