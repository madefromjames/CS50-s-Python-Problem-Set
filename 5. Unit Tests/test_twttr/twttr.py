user = input("Input: ")

def shorten(word):
    vowel = "aeiouAEIOU"
    for _ in vowel:
        table = str.maketrans('', '', vowel)
        new_string = word.translate(table)
        return new_string

modify = shorten(user)
print(f"Output: {modify}")