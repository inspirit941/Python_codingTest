def check_shape(start, color, row_num, board):
    y, x = start
    color = board[y][x]
    coord = set()
    color_cnt, black_cnt = 0, 0
    if row_num == 2 and y - 2 >= 0:
        # [1,#],
        # [1,#],
        # [1,1] 와 같은 형태
        for cx in range(x, x-2, -1):
            for cy in range(y, y-3, -1):
                if cy >= 0 and (board[cy][cx] == color or board[cy][cx] == '#'):
                    if board[cy][cx] == color: color_cnt += 1
                    if board[cy][cx] == '#': black_cnt += 1
                    coord.add((cy, cx))
                else:
                    return None
        if color_cnt == 4 and black_cnt == 2:
            return coord
        else:
            return None
    # [1,0,0], 
    # [1,1,1] 와 같은 형태
    if row_num == 3 and y-1 >= 0:
        for cx in range(x, x-3, -1):
            for cy in range(y, y-2, -1):
                if cy >= 0 and (board[cy][cx] == color or board[cy][cx] == '#'):
                    if board[cy][cx] == color: color_cnt += 1
                    if board[cy][cx] == '#': black_cnt += 1
                    coord.add((cy, cx))
                else:
                    return None
        # 블록 개수 4개, 검은 블록 2개일 경우에만 제거 가능.
        if color_cnt == 4 and black_cnt == 2:
            return coord
        else:
            return None
    
    return None
def build(board):
    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[y][x] == '#':
                continue
            if board[y][x] == 0:
                board[y][x] = '#'
            elif board[y][x] != 0:
                break
def search_shape(board):
    for y in range(len(board)-1, -1, -1):
        consecutive = 0
        color = None
        for x in range(len(board[0])):
            if board[y][x] == 0:
                color = None
                consecutive = 0
                continue
            if type(board[y][x]) is int and board[y][x] != 0:
                if color == None:
                    consecutive = 1
                    color = board[y][x]
                    continue
                if board[y][x] != color:
                    color = board[y][x]
                    consecutive = 1
                    continue
                if color == board[y][x]:
                    consecutive += 1
                
                if 2 <= consecutive <= 3:
                    coord = check_shape((y,x), color, consecutive, board)
                    if coord is not None:
                        return coord
    return None
                
def remove(board, coord):
    for y, x in coord:
        board[y][x] = 0
        
def solution(board):
    cnt = 0
    while True:
        # 1. 조건상 채울 수 있는 모든 공간에 검은 블록 채워넣기
        build(board)
        # 2. 검은 블록 + 블록으로 제거될 수 있는 블록 찾기
        coord = search_shape(board)
        # 찾을 수 없는 경우 break
        if coord is None:
            break
        # 제거 블록개수 + 1
        cnt += 1
        # 블록 제거하기
        remove(board, coord) 
        
    return cnt