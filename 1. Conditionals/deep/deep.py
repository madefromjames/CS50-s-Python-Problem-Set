user = input("What is the Answer to the Greatest Question of Life, the Universe, and Everything? ")

case = user.casefold().replace(' ', '')

if case == '42' or case == 'forty-two' or case == 'fortytwo':
    print("Yes")
else:
    print("No")
