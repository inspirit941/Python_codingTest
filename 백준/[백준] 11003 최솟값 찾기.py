import sys
from collections import deque
n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(n)]
window = deque()
for idx in range(n):
    # window의 마지막 값보다 input으로 넣을 값이 작은 경우
    # 최솟값은 어차피 input값이 될 것이므로, window에 굳이 넣을 필요가 없다
    while window and window[-1][1] > arr[idx]:
        window.pop()
    # window 최솟값의 index가 현재 window 크기를 벗어난 경우
    # 값을 빼 준다.
    while window and idx - window[0][0] >= l:
        window.popleft()
    window.append((idx, arr[idx]))
    d[idx] = window[0][1]
print(*d)