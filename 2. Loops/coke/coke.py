_insert = 0
while _insert < 50:
    insert = int(input("Insert Coin: "))
    coins = [25, 10, 5]

    if insert in coins:
        _insert += insert
        amt_due = 50 - _insert
        if amt_due > 0:
            print(f"Amount Due: {amt_due}")
        else:
            change = abs(amt_due)
            print(f"Change Owed: {change}")
    elif coins != insert:
        change = abs(50)
        print(f"Amount Due: {change}")
