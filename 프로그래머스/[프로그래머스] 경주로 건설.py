import math
from collections import deque

def solution(board):
    def bfs(start):
        # table[y][x] = 해당 위치에 도달하는 최솟값.
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
        # 위 - 0, 왼쪽 - 1, 아래 = 2, 오른쪽 = 3
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        queue = deque([start])
        # (cost, y, x, head)
        table[0][0] = 0
        answer = math.inf
        while queue:
            y, x, cost, head = queue.popleft()
            for idx, (dy, dx) in enumerate(dirs):
                ny, nx = y + dy, x + dx
                n_cost = cost + 600 if idx != head else cost + 100
                if 0 <= ny < len(board) and 0 <= nx < len(board) and board[ny][nx] == 0 and table[ny][nx] > n_cost:
                    table[ny][nx] = n_cost
                    queue.append((ny, nx, n_cost, idx))
        return table[-1][-1]
    return min(bfs((0,0,0,2)), bfs((0,0,0,3)))