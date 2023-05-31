grid = []
number = 1
for x in range(3):
    l = []
    for y in range(3):
        l.append(number)
        number += 1
    grid.append(l)
grid[-1][-1] = 0

print(grid)