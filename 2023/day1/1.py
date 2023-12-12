import numpy as np

with open('data.txt') as f:
    lines = [line.rstrip() for line in f]

first = np.array([])
last = np.array([])
for line in lines:
    i = 0
    for letter in line:
        if letter.isdigit() and i == 0:
            i += 1
            first = np.append(first, letter)

for line in lines:
    line = line[::-1]
    i = 0
    for letter in line:
        if letter.isdigit() and i == 0:
            i += 1
            last = np.append(last, letter)
calibration = np.array([])
for (f, l) in zip(first, last):
    calibration = np.append(calibration, int(str(f)+str(l)))
print(sum(calibration))  # correct
