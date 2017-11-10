from tower import Tower

towers = [0]*3
capacity = 5
for i in range(0, 3):
    towers[i] = Tower(i)

for i in range(capacity-1, -1, -1):
    towers[0].add(i)

towers[0].move_disks(capacity, towers[2], towers[1])