while True:
    div = None

    try:
        x = input("Fraction: ")
        num, den = map(int, x.split("/"))
        div = num / den * 100
    except ValueError:
        print("This is a Value Error")
    except ZeroDivisionError:
        print("This is a Division Error")
        continue

    if div is not None:
        if div <= 1:
            print("E")
            break
        elif 99 <= div <= 100:
            print("F")
            break
        elif div > 100:
            continue
        else:
            print(f"{int(round(div))}%")
            break
