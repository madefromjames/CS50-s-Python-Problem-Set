user = input("Item: ")
fruits = {
    'Apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Sweet Cherries': 100,
    'Kiwifruit': 90,
    'Pear': 100,
    'Sweet Cherries': 100
}

# Loop through dictionary keys
for fruit in fruits:
    if user == fruit.capitalize() or user == fruit.casefold() or user == fruit.title():
        print(f"Calories: {fruits[fruit]}")
