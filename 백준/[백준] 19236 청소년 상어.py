import sys
from copy import deepcopy
dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
maps = [[0 for _ in range(4)] for _ in range(4)]

fish_dict = dict()
y, x = 0, 0
for _ in range(4):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(0, len(arr), 2):
        fish, head = arr[i], arr[i+1]-1
        maps[y][x] = [fish, head]
        fish_dict[fish] = (y, x)
        x += 1
    y += 1
    x = 0

# 초기값. 0,0 위치
result = 0

def no_fish():
    return [0, None]


def dfs(shark_pos, maps, score, fish_dict):
    global result
    
    # 현재 위치의 물고기 잡음
    y_s, x_s = shark_pos
    shark_heading = maps[y_s][x_s][1]
    got_fish = maps[y_s][x_s][0]
    # 잡은 물고기는 빈 공간으로
    fish_dict.pop(maps[y_s][x_s][0])
    maps[y_s][x_s] = no_fish()

    # 물고기 이동
    for f_num in range(1, 17):
        # 없는 물고기일 경우 패스
        if f_num not in fish_dict:
            continue
        y, x = fish_dict[f_num]
        # 이동할 수 없는 경우: 이동할 수 있을 때까지 확인
        can_move = False
        for _ in range(9):
            heading = dirs[maps[y][x][1]]
            ny, nx = y + heading[0], x + heading[1]
            # 공간 경계 안에 있으면서, 물고기가 이동할 수 있는 공간인 경우
            if (0 <= ny < len(maps) and 0 <= nx < len(maps[0])) and (0 <= maps[ny][nx][0] <= 16) \
            and ((ny, nx) != (y_s, x_s)):
                can_move = True
                break
            else:
                maps[y][x][1] = (maps[y][x][1]+1) % 8
        
        if not can_move:
            continue
            
        # 비어 있을 경우 - 해당 위치로 이동
        if maps[ny][nx][0] == 0:
            maps[ny][nx] = maps[y][x]
            fish_dict[f_num] = (ny, nx)
            maps[y][x] = no_fish()
            
        
        else:
            # 기존 물고기와 자리바꿈
            o_num = maps[ny][nx][0]
            maps[ny][nx], maps[y][x] = maps[y][x], maps[ny][nx]
            fish_dict[f_num] = (ny, nx)
            fish_dict[o_num] = (y, x)
    
    # 상어가 이동할 다음 좌표
    ny, nx = y_s + dirs[shark_heading][0], x_s + dirs[shark_heading][1]

    # 다음 좌표로 이동이 가능한 경우
    while 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
        # 물고기가 있는 좌표일 경우 - dfs로 재귀탐색 진행
        if maps[ny][nx][0] != 0:
            dfs([ny, nx], deepcopy(maps), score+got_fish, deepcopy(fish_dict))
        
        # maps[ny][nx][0] == 0 인 경우는 해당 위치에 물고기가 없는 경우이다.
        # 다음 좌표로 이동
        ny, nx = ny + dirs[shark_heading][0], nx + dirs[shark_heading][1]
    
    # 더 이상 잡을 수 있는 물고기가 없는 경우 - 최댓값 갱신
    result = max(result, score+got_fish)
    return
    
    
dfs([0,0], maps, 0, fish_dict)
print(result)