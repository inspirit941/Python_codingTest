import sys
from collections import deque
maps = []
birds = []
r, c = map(int, sys.stdin.readline().split())
for y in range(r):
    arr = list(sys.stdin.readline().replace("\n",""))
    maps.append(arr)
    for x in range(len(arr)):
        if arr[x] == "L":
            birds.append((y, x))

# 해당위치는 몇 초 후에 전부 녹는지를 저장한 배열
time = [[0 for _ in range(c)] for _ in range(r)]

# 빙하가 녹는 시간대를 time에 저장하고
# 가장 마지막으로 빙하가 녹은 시간이 몇 초인지를 리턴하는 함수
def melt_time_set(maps: list) -> int:
    visited = [[False for _ in range(c)] for _ in range(r)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    # 처음에 바다이거나 백조인 부분
    queue = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == '.' or maps[y][x] == 'L':
                queue.append((y, x))
                time[y][x] = 0
                visited[y][x] = True
    
    # 마지막으로 빙하가 녹은 시간
    last_time = 0
    # 각 위치의 빙하가 녹는 데 몇 초가 필요한지
    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "L":
                queue.append((ny, nx))
                time[ny][nx] = time[y][x] + 1
                visited[ny][nx] = True
                last_time = time[ny][nx]
    return last_time
# bfs(백조1 위치, 빙하, 이분탐색 기준값, 백조2 위치)
def bfs(start: tuple, maps: list, mid: int, end : tuple) -> bool:
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque()
    queue.append(start)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
                visited[ny][nx] = True
                # 백조1이 백조2 위치에 도착할 수 있는 경우
                if ny == end[0] and nx == end[1]:
                    return True
                # 기준 시간초인 mid보다 작은 빙하는 녹아서 이동가능한 것으로 간주
                if time[ny][nx] <= mid:
                    queue.append((ny, nx))
    return False

_min, _max = 0, melt_time_set(maps)
answer = _max
while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(birds[0], maps, mid, birds[1]):
        answer = mid
        _max = mid - 1
    else:
        _min = mid + 1
print(answer)
