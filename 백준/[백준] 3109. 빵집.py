import sys
r, c = map(int, sys.stdin.readline().split())
maps = []
for y in range(r):
    arr = list(sys.stdin.readline().replace("\n",""))
    maps.append(arr)

# 많은 파이프를 심으려면, 최대한 우상향으로 접근해야 함.
dirs = [(-1,1),(0,1),(1,1)]
end_line = len(maps[0])-1

def connect_pipe(y: int, x: int) -> bool:
    # 현재 위치에 파이프 생성
    maps[y][x] = 'x'
    if x == end_line:
        return True
    
    for dy, dx in dirs:
        ny, nx = y+dy, x+dx
        # 다음 위치에 파이프 생성이 가능한지 확인
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == ".":
            if connect_pipe(ny, nx):
                # 끝까지 설치가 가능할 경우 이 분기로 진입하게 됨.
                return True
    return False

answer = 0
for y in range(len(maps)):
    if connect_pipe(y,0):
        answer += 1
print(answer)
    