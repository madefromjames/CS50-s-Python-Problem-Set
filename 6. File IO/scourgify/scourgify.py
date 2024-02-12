import sys
import csv

def main():
    cmdline()
    # append the changes of the readable file
    output = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                change = row['name'].split(',')
                # rearranged the order of format to output list
                output.append({'first': change[1].lstrip(), 'last': change[0], 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], 'w') as file:
        # Dictionary keys
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writing to the first row of the file
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        # looping through output and writing to the new file
        for row in output:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

def cmdline():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()