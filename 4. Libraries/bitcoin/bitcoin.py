import requests
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()
    try:
        bitcoin = r['bpi']['USD']['rate_float']
        total = bitcoin * value
        print(f"${total:,.4f}")
    except ValueError:
        print("Value Error")
        sys.exit(1)
except requests.RequestException:
    print("Request Exception")
    sys.exit(1)