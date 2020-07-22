import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
connected = defaultdict(set)
for _ in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    connected[parent].add(child)
    connected[child].add(parent)
    
def bfs(start, connected, end):
    visited = set()
    queue = deque()
    queue.append((0, start))
    while queue:
        cnt, p = queue.popleft()
        visited.add(p)
        if p == end:
            return cnt
        for nxt in connected[p]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((cnt+1, nxt))
    return -1

print(bfs(a, connected, b))