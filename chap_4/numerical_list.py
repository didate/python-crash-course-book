for value in range(1, 5):  # 1 to 4
    print(value)
print("------------------------------")
for value in range(1, 6):  # 1 to 5
    print(value)

print("------------------------------")
numbers = list(range(1, 6))
print(numbers)

print("------------------------------")
for value in range(2, 11, 2):
    print(value**2)  # Square of values
print("------------------------------")
digits = list(range(1, 10))
print("Max of list is : " + str(max(digits)))
print("Min of list is : " + str(min(digits)))
print("Sum of list is : " + str(sum(digits)))

print("------------------------------")
squares = [value**2 for value in range(1, 11)]
print(squares)
