import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    randomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
    randomFont = False
else:
    sys.exit("Invalid")

user = input("Input: ")

if randomFont == False:
    figlet.setFont(font=sys.argv[2])
elif randomFont == True:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)

print("Output:")
print(figlet.renderText(user))