from math import factorial
def solution(n, k):
    # 1번부터 n번까지 번호 배열
    numbers = list(range(1, n+1))
    # 총 사람 수
    length = len(numbers)
    result = []
    while len(result) != length:
        # 앞자리부터 조건에 부합하는 숫자 찾기 = 나머지 숫자들을 가지고 경우의 수 확인.
        n -= 1
        # idx = 몇 번째 숫자가 맨 앞에 오는지, rest = 다음 순서
        idx, rest = divmod(k, factorial(n))
        # rest가 0이면 정확히 나누어떨어졌다는 뜻이므로, 몫의 위치를 조정해야 한다.
        if rest == 0:
            idx -= 1
        # 해당 위치의 숫자를 저장하고, 남은 숫자 목록에서 해당 위치의 숫자를 제거한다.
        result.append(numbers[idx])
        numbers.remove(numbers[idx])
        # 다음 탐색을 위해 k값을 변경한다.
        k = rest
    return result