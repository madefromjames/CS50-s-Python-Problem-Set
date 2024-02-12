from tabulate import tabulate
import sys
import csv

def main():
    cmdline()
    pizzas = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for pizza in reader:
                pizzas.append(pizza)
    except FileNotFoundError:
        sys.exit("File does not exist")
ls
    print(tabulate(pizzas[1:], headers=pizzas[0], tablefmt="grid"))

def cmdline():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()