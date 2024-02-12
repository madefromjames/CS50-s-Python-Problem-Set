import random

while True:
    try:
        _level = input("Level: ")
        # rejects non-numeric level
        if not _level.isdigit():
            continue

        level = int(_level)

        # Negative integer should prompt again
        if level < 1:
            continue

        # Randomly generates int between 1 and level
        random_int = random.randint(1, level)
        probability = random_int

        # User guess for probability
        while True:
            _guess = input("Guess: ")

            # rejects non-numeric guess
            if not _guess.isdigit():
                continue

            guess = int(_guess)

            if guess == probability:
                print("Just right!")
                break
            elif guess < probability:
                print("Too small!")
            else:
                print("Too large!")
    except ValueError:
        print("Enter a correct digit")
    break