players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Slice from index 3 to index 4 (without index 4)=> [florence]
print(players[3:4])

print(players[:4])  # from the beginning to index 4

print(players[4:])  # from index 4 to the end

my_foods = ['pizza', 'falafel', 'carrot cake']
print("My Food List :")
print(my_foods)
friend_foods = my_foods[:]
print("My Friends Food List :")
print(friend_foods)
