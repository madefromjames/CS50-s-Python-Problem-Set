def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # “All vanity plates must start with at least two letters.”
    if not s[:2].isalpha() :
        return False
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) > 6 or len(s) < 2:
        return False
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    if s[-1].isdigit() and (len(s) < 3 or not s[-2].isdigit()):
        return False
    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
    # “No periods, spaces, or punctuation marks are allowed.”
    if s in ['.', ' ', '!', '?']:
        return False

    return True
if __name__ == "__main__":
    main()