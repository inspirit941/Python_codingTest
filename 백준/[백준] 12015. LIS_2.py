import sys
import bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

table = [arr[0]]
for idx in range(1, n):
    # 현재까지의 부분수열 최댓값보다 더 큰 값일 경우
    if arr[idx] > table[-1]:
        table.append(arr[idx])
    else:
        # 현재 값이 부분수열의 어느 부분에 해당하는지 - left idx로 확인
        insert_idx = bisect.bisect_left(table, arr[idx])
        # 해당 위치의 값 업데이트
        table[insert_idx] = arr[idx]
# 최장 부분수열의 길이
print(len(table))