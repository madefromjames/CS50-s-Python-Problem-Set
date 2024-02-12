def main():
    x = input("Fraction: ")
    fraction = convert(x)
    gauge_value = gauge(fraction)
    print(gauge_value)


def convert(fraction):
    while True:
        try:
            num, den = map(int, fraction.split("/"))
            div = num / den
            if div <= 1:
                div = int(div * 100)
                return div
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage) + '%'


if __name__ == "__main__":
    main()