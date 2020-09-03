import math

def solution(matrix_sizes):
    # table[start][end] = 인덱스 start ~ end 까지의 연산 최솟값.
    table = [[math.inf for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]
    # start와 end가 동일한 경우는 연산하지 않으므로 0으로 설정.
    for idx in range(len(matrix_sizes)):
        table[idx][idx] = 0
    
    for gap in range(1, len(matrix_sizes)):
        for start in range(len(matrix_sizes)):
            end = start + gap
            if end >= len(matrix_sizes):
                break
            for sep in range(start, end):
                table[start][end] = min(
                    table[start][end],
                    table[start][sep] + table[sep+1][end] + (matrix_sizes[start][0] * matrix_sizes[sep][1] * matrix_sizes[end][1])
                )
    return table[0][-1]
        