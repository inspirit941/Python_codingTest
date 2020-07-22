import sys
from collections import deque
# F : 건물의 총 높이
# G : 목적지
# U : 위로 한 번에 이동할 수 있는 폭
# D : 아래로 한 번에 이동할 수 있는 폭
# 현재위치 = S.
F, S, G, U, D = map(int, sys.stdin.readline().split())

def bfs(start, end, up, down, F):
    visited = set()
    queue = deque()
    queue.append((0, start))
    visited.add(start)
    while queue:
        cnt, stairs = queue.popleft()
        if stairs == end:
            return cnt
        if stairs + up <= F and stairs + up not in visited:
            visited.add(stairs+up)
            queue.append((cnt+1, stairs+up))
        if stairs - down >= 1 and stairs - down not in visited:
            visited.add(stairs-down)
            queue.append((cnt+1, stairs-down))
    
    return "use the stairs"

print(bfs(S, G, U, D, F))
