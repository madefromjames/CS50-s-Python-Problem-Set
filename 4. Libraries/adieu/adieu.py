import inflect

p = inflect.engine()

names = list()

while True:
    try:
        user = input("Name: ")
        names.append(user)
    except EOFError:
        print()
        break

output = p.join(names)
print(f"Adieu, adieu, to {output}")

