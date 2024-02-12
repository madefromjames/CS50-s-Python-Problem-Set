import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    work = re.search(r"^(([0-9][0-2]*):?([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):?([0-5][0-9])*) ([A-P]M)$", s)
    if work:
        time = work.groups()
        if int(time[1]) > 12 or int(time[5]) > 12:
            raise ValueError
        time1 = time_format(time[1], time[2], time[3])
        time2 = time_format(time[5], time[6], time[7])
        return time1 + " to " + time2
    else:
        raise ValueError("Invalid Input")

def time_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = "00"
        new_time = f"{new_hour:02}" + ":" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time


if __name__ == "__main__":
    main()