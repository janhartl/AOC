import numpy as np

with open('data.txt') as f:
    lines = [line.rstrip() for line in f]

numbers = ["one", "two", "three", "four", "five",
           "six", "seven", "eight", "nine"]
inumbers = ["eno", "owt", "eerht", "ruof", "evif",
            "xis", "neves", "thgie", "enin"]

first = np.array([])
last = np.array([])
for line in lines:
    i = 0
    text = ""
    for letter in line:
        if letter.isdigit() and i == 0:
            i += 1
            first = np.append(first, letter)
        if i == 0:
            text = text+letter
            for number in numbers:
                if number in text:
                    i += 1
                    first = np.append(first, 1 + numbers.index(number))


for line in lines:
    line = line[::-1]
    i = 0
    text = ""
    for letter in line:
        if letter.isdigit() and i == 0:
            i += 1
            last = np.append(last, letter)
        if i == 0:
            text = text+letter
            for inumber in inumbers:
                if inumber in text:
                    i += 1
                    last = np.append(last, 1 + inumbers.index(inumber))
calibration = np.array([])
for (f, l) in zip(first, last):
    calibration = np.append(calibration, int(str(f)+str(l)))
print(calibration, np.sum(calibration))
