import sys
from collections import defaultdict
# taller[i] = i보다 키 큰 사람의 집합
# shorter[i] = i보다 키 작은 사람의 집합
taller, shorter = defaultdict(set), defaultdict(set)

n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    # a는 b보다 키가 작다
    a, b = map(int, sys.stdin.readline().split())
    taller[a].add(b)
    shorter[b].add(a)
    
    
for i in range(1, n+1):
    # i보다 작은 사람 -> i보다 큰 사람보다는 반드시 작다.
    for shorter_than_i in shorter[i]:
        taller[shorter_than_i].update(taller[i])
    # i보다 큰 사람 -> i보다 작은 사람보다는 반드시 크다.
    for taller_than_i in taller[i]:
        shorter[taller_than_i].update(shorter[i])
    
result = 0
for i in range(1, n+1):
    if len(taller[i]) + len(shorter[i]) == n-1:
        result += 1
print(result)
