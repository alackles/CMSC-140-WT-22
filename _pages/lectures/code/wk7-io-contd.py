from pathlib import Path
import matplotlib.pyplot as plt

filedir = Path("data")
filepath = filedir / "temps.txt"
hellopath = filedir / "hello.txt"

temps = []
hats = []
with open(filepath) as f:
    next(f)
    for line in f.readlines(): # iterates through every line of the file
        line = line.strip().split(" ") # strips out whitespace on every line and then splits
        t, h = line # assigns t and h to the first and second elements of the list line
        temps.append(int(t)) # appends t as an integer to the list temps
        hats.append(int(h)) # appends h as an integer to the list hats
print(temps)
print(hats)

plt.scatter(temps, hats)
plt.show()
