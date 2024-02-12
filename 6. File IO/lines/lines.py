import sys

if len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as f:
                lines = [line for line in f if line.strip() and not line.strip().startswith('#')]
                print(len(lines))
        except FileNotFoundError:
            sys.exit("File does not exist")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")