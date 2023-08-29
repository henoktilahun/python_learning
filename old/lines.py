import sys
import os

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

lines = []
count = 1

with open(sys.argv[1]) as file:
    for line in file:
        lines.append(line.rstrip())
    print(lines)