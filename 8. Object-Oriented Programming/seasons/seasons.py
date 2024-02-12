from datetime import date
import re
import sys
import inflect
import operator

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = birthday(birth_date)
    except:
        sys.exit("Invalid Date")
    today = date(int(year), int(month), int(day))
    today_date = date.today()
    date_diff = operator.sub(today_date, today)
    minutes = date_diff.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize() + " minutes")



def birthday(birth_date):
    if re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()