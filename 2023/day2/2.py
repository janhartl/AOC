#  i love u baby
import numpy as np
with open('data.txt') as f:
    lines = [line.rstrip() for line in f]

games = np.array([])  # index, r, g, b

split_lines = []
for line in lines:
    split_lines.append(line.split(":"))

split_lines = np.array(split_lines).T
games = split_lines[0]

cs = split_lines[1]
cs = np.char.split(cs, ";")
pulls_bygame = []
red, green, blue = 0, 0, 0

multiplied = []

for line in cs:
    line = np.char.split(line, ",")
    pulls_bygame.append(line)
bad_games = []
for i, game in enumerate(pulls_bygame):
    red, green, blue = 0, 0, 0
    for element in game:
        for instance in element:
            if instance[2].isdigit():
                alpha = instance[1] + instance[2]
            else:
                alpha = instance[1]
            alpha = int(alpha)

            if "red" in instance:
                red = max(red, alpha)
                if alpha > 12:
                    if i+1 not in bad_games:
                        bad_games.append(i+1)

            if "green" in instance:
                green = max(green, alpha)
                if alpha > 13:
                    if i+1 not in bad_games:
                        bad_games.append(i+1)

            if "blue" in instance:
                blue = max(blue, alpha)
                if alpha > 14:
                    if i+1 not in bad_games:
                        bad_games.append(i+1)
    multiplied.append(red*green*blue)

print(5050-sum(bad_games))
print(sum(multiplied))
