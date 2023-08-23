months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user = input("Date: ").title().strip()
    try:
        month, day, year = user.split('/')
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            nmonth, nday, year = user.split(' ')
            for x in range(len(months)):
                if nmonth == months[x]:
                    month = x + 1
            if ',' not in nday:
                continue
            day = nday.replace(',','')
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
