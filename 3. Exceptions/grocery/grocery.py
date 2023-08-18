justrite = {
    'Apple': 0,
    'Banana': 0,
    'Strawberry': 0,
    'Milk': 0,
    'Mango': 0,
    'Sugar': 0,
    'Tortilla': 0,
    'Sweet Potato': 0
}

add = 0
while True:
    try:
        user = input("")
        if user.title() in justrite:
            justrite[user.title()] += 1
    except EOFError:
        break

sorted_items = sorted(justrite.items())
for key, value in sorted_items:
    if value > 0:
        print(f"{value} {key.upper()}")
