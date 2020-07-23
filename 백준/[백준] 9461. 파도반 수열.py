import sys
n = int(sys.stdin.readline())
memo = {1:1,2:1,3:1,4:2,5:2}
def find_result(number : int) -> int:
    if number in memo:
        return memo[number]
    memo[number] = find_result(number-1) + find_result(number-5)
    return memo[number]

for _ in range(n):
    num = int(sys.stdin.readline())
    print(find_result(num))