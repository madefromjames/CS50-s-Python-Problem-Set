def main():
    user = input("What time is it? ")
    if 7.0 <= convert(user) <= 8.0:
        print('breakfast time')
    elif 12.0 <= convert(user) <= 13.0:
        print('lunch time')
    elif 18.0 <= convert(user) <= 19.0:
        print('dinner time')


def convert(time):
   hours, minutes = time.split(":")
   if "AM" in time or "PM" in time:
        minutes = minutes.replace("AM", "").replace("PM", "")
        if "PM" in time:
            hours = float(hours) + 12
   return float(hours) + float(minutes) / 60.0


if __name__ == "__main__":
    main()
