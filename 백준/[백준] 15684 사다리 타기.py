import sys
n, m, h = map(int, sys.stdin.readline().split())
table = [[0 for _ in range(n+2)]  for _ in range(h)]
# table[y][x] = x와 x+1이 y번째 row에서 연결되어 있다.
answer = 4
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    table[a-1][b] = 1

def check(maps):
    # col은 1부터 len(maps[0])-2개까지.
    for col in range(1, len(maps[0])-2):
        start = col
        for row in range(len(maps)):
            if maps[row][col] == 1:
                col += 1
            elif maps[row][col-1] == 1:
                col -= 1
        # 도착지점과 시작지점의 column이 다른 경우
        if col != start:
            return False
    return True
       
def ladder_build_and_search(maps, cnt, limit):
    global answer
    if cnt == limit:
        if check(maps):
            answer = min(answer, limit)
        return
    for y in range(len(maps)):
        for x in range(1, len(maps[0])-2):
            if maps[y][x] != 1 and maps[y][x-1] != 1 and maps[y][x+1] != 1:
                maps[y][x] = 1
                ladder_build_and_search(maps, cnt+1, limit)
                maps[y][x] = 0
                
for i in range(4):
    ladder_build_and_search(table, 0, i)
    if answer != 4:
        break
if answer != 4:
    print(answer)
else:
    print(-1)