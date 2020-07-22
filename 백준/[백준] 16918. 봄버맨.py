import sys
from collections import deque
r, c, n = map(int, sys.stdin.readline().split())
bombs = []
maps = []
for y in range(r):
    maps.append(list(sys.stdin.readline().replace("\n","")))
    for x in range(len(maps[0])):
        if maps[y][x] == 'O':
            maps[y][x] = (0+3, maps[y][x])
        else:
            maps[y][x] = (0, maps[y][x])

def spread(time):
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x][1] == '.':
                maps[y][x] = (time+3, 'O')

def explode(time):
    bombs = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x][0] == time:
                bombs.append((y,x))
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    while bombs:
        y, x = bombs.popleft()
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                maps[ny][nx] = (time, ".")
        maps[y][x] = (time, ".")

time = 1
build = True
while time <= n:
    if time == 1:
        time += 1
        continue
    if build:
        build = False
        spread(time)
    else:
        build = True
        explode(time)
    time += 1

for y in range(len(maps)):
    print("".join([i[1] for i in maps[y]]))