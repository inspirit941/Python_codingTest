from collections import deque
def solution(board):
    def bfs(start):
        queue = deque()
        queue.append((start, 0))
        visited = set()
        while queue:
            coord, cnt = queue.popleft()
            # 현재 비행기 위치좌표 저장
            visited.add(tuple(coord))
            left, right = coord[0], coord[1]
            if right[0] == len(board)-1 and right[1] == len(board)-1:
                return cnt
            
            ## 비행기가 가로로 있는 경우
            if left[0] == right[0]:
                # 왼쪽으로 1 이동
                new_coord = ((left[0], left[1]-1), (left[0], left[1]))
                # 왼쪽으로 1 이동한 좌표가 board 범위 내에 있고, 아직 방문한 좌표가 아니며, board값이 0인 경우
                if 0 <= new_coord[0][1] < len(board) and new_coord not in visited and board[new_coord[0][0]][new_coord[0][1]] == 0:
                    visited.add(new_coord)
                    queue.append((new_coord, cnt+1))
                
                # 오른쪽으로 1 이동
                new_coord = ((right[0], right[1]),(right[0], right[1]+1))
                if 0 <= new_coord[1][1] < len(board) and new_coord not in visited and board[new_coord[1][0]][new_coord[1][1]] == 0:
                    visited.add(new_coord)
                    queue.append((new_coord, cnt+1))
                    
                # 위/아래 이동
                for dy in [-1,1]:
                    new_coord = ((left[0] + dy, left[1]), (right[0]+dy, right[1]))
                    if 0 <= new_coord[0][0] < len(board) and new_coord not in visited and board[new_coord[0][0]][new_coord[0][1]] == board[new_coord[1][0]][new_coord[1][1]] == 0:
                        visited.add(new_coord)
                        queue.append((new_coord, cnt+1))

                # 회전
                for dy in [-1,1]:
                    # 왼쪽 좌표 기준으로 회전하는 경우
                    # 오른쪽 좌표의 위/아래 좌표가 board 범위내에 있고 값이 0일 경우 = 회전이 가능하다.
                    if 0 <= right[0] + dy < len(board) and board[right[0]+dy][right[1]] == 0:
                        # 새로운 오른쪽 좌표를 생성하고, 정렬해준다
                        new_r = (left[0]+dy, left[1])
                        new_coord = tuple(sorted([left, new_r], key = lambda x: (x[0],x[1])))
                        if 0 <= new_r[0] < len(board) and board[new_r[0]][new_r[1]] == 0 and new_coord not in visited:
                            visited.add(new_coord)
                            queue.append((new_coord, cnt+1))
                            
                    # 오른쪽 좌표 기준 회전
                    # 왼쪽 좌표의 위/아래 좌표가 board 범위내에 있고 값이 0일 경우 = 회전이 가능하다
                    if 0 <= left[0]+dy < len(board) and board[left[0]+dy][left[1]] == 0:
                        new_l = (right[0]+dy, right[1])
                        new_coord = tuple(sorted([new_l, right], key = lambda x: (x[0], x[1])))
                        if 0 <= new_l[0] < len(board) and board[new_l[0]][new_l[1]] == 0 and new_coord not in visited:
                            visited.add(new_coord)
                            queue.append((new_coord, cnt+1))
                            
            ## 비행기가 세로로 있는 경우
            if left[1] == right[1]:
                # 위로 이동
                new_coord = ((left[0]-1, left[1]),(left[0], left[1]))
                if 0 <= new_coord[0][0] < len(board) and new_coord not in visited and board[new_coord[0][0]][new_coord[0][1]] == 0:
                    visited.add(new_coord)
                    queue.append((new_coord, cnt+1))
                # 아래로 이동
                new_coord = ((right[0], right[1]), (right[0]+1, right[1]))
                if 0 <= new_coord[1][0] < len(board) and new_coord not in visited and board[new_coord[1][0]][new_coord[1][1]] == 0:
                    visited.add(new_coord)
                    queue.append((new_coord, cnt+1))
                # 좌우로 이동
                for dx in [-1,1]:
                    new_coord = ((left[0], left[1]+dx), (right[0], right[1]+dx))
                    if 0 <= new_coord[0][1] < len(board) and new_coord not in visited and board[new_coord[0][0]][new_coord[0][1]] == board[new_coord[1][0]][new_coord[1][1]] == 0:
                        visited.add(new_coord)
                        queue.append((new_coord, cnt+1))
                
                # 회전
                for dx in [-1,1]:
                    # 위쪽 기준으로 회전
                    # 아래쪽 값의 좌/우 좌표가 board 범위 내에 있고, 값이 0일 경우 회전 가능
                    if 0 <= right[1] + dx < len(board) and board[right[0]][right[1]+dx] == 0:
                        # 변경된 좌표를 생성하고, 정렬해준다.
                        new_r = (left[0], left[1]+dx)
                        new_coord = tuple(sorted([left, new_r], key = lambda x: (x[0],x[1])))
                        if 0 <= new_r[0] < len(board) and board[new_r[0]][new_r[1]] == 0 and new_coord not in visited:
                            visited.add(new_coord)
                            queue.append((new_coord, cnt+1))
                    # 아래쪽 좌표 기준 회전
                    # 위쪽 값의 좌/우 좌표가 board 범위 내에 있고, 값이 0일 경우 회전 가능
                    if 0 <= left[1]+dx < len(board) and board[left[0]][left[1]+dx] == 0:
                        new_l = (right[0], right[1]+dx)
                        new_coord = tuple(sorted([new_l, right], key = lambda x: (x[0], x[1])))
                        if 0 <= new_l[0] < len(board) and board[new_l[0]][new_l[1]] == 0 and new_coord not in visited:
                            visited.add(new_coord)
                            queue.append((new_coord, cnt+1))
                    


    return bfs( ((0,0),(0,1)) )