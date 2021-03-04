fruit_bowl = {}

fruit_bowl["apple"] = 4
fruit_bowl["banana"] = 2

print(fruit_bowl)

user_input = input("What kind of fruit will you add?")
fruit_bowl[user_input] = fruit_bowl.get(user_input, 0) + 1

for fruit, amount in fruit_bowl.items():
    print(fruit, amount)
