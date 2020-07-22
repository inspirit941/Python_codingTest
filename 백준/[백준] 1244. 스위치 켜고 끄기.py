import sys
# 남 : 스위치번호가 자기 배수이면, 상태 바꾼다.
# 여 : 현 위치 중심으로 좌우대칭이면서 가장 많은 스위치를 포함하는 구간 전부 바꿈.
SPLITS = 20

# 좌우대칭이면서 가장 긴 거리 찾는 함수
def find_symmetric(arr, idx):
    r, l = idx - 1, idx + 1
    min_r, max_l = idx, idx
    while r > 0 and l < len(arr):
        if arr[r] == arr[l]:
            min_r, max_l = r, l
            r -= 1
            l += 1
        else:
            break
    return max(idx - min_r, max_l - idx)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# 계산편의를 위해 index 0에 값 삽입
arr.insert(0, -1)
n = int(sys.stdin.readline())
for _ in range(n):
    sex, idx = map(int, sys.stdin.readline().split())
    # 남자
    if sex == 1:
        for idx in range(idx, len(arr), idx):
            arr[idx] = (arr[idx] + 1) % 2
    # 여자
    elif sex == 2:
        width = find_symmetric(arr, idx)
        temp = arr[idx-width : idx+width + 1]
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 2
        arr[idx-width:idx+width+1] = temp
for idx in range(1, len(arr), SPLITS):
    print(*arr[idx:idx+SPLITS])