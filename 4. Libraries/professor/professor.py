import random


def main():
    level = get_level()
    score = 0

    for counting in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for counting in range(3):
            calc = int(input(f"{x} + {y} = "))
            if calc == answer:
                score += 1
                break
            else:
                print("EEE")
                counting += 1

        else:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
    return x



if __name__ == "__main__":
    main()