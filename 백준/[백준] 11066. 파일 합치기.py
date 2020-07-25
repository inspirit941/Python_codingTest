import sys
import math
#sys.stdin = open('input.txt')
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    # i번째 페이지까지의 연속합
    cumsum = {-1:0}
    for i in range(len(arr)):
        cumsum[i] = cumsum[i-1] + arr[i]
        
    dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    
    # gap : 시작페이지 - 끝페이지 간 거리.
    for gap in range(1, len(arr)):
        # start : 페이지 시작지점
        for start in range(len(arr)):
            # end : 페이지 끝지점
            end = start + gap
            # 범위를 벗어난 경우
            if end == len(arr):
                break
            dp[start][end] = math.inf
            for i in range(start, end):
                dp[start][end] = min(
                            dp[start][end],
                            dp[start][i] + dp[i+1][end] + cumsum[end] - cumsum[start-1]
                                    )
    print(dp[0][-1])