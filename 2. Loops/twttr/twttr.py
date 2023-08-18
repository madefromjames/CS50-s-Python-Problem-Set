user = input("Input: ")

def change(insert):
    vowel = "aeiouAEIOU"
    for _ in vowel:
        table = str.maketrans('', '', vowel)
        new_string = insert.translate(table)
        return new_string

modify = change(user)
print(f"Output: {modify}")
