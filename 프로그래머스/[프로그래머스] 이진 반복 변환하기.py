from collections import Counter
def solution(s):
    # 0 개수, 반복 횟수를 저장
    zeros, cnt = 0, 0
    while s != "1":
        # 횟수 카운트
        cnt += 1
        # 제거한 0의 개수 저장
        zeros += Counter(s)['0']
        # 1의 개수를 정수로 변환 -> bin()으로 이진수 변환 -> str로 문자열 변환.
        # bin으로 이진수 변환 시 앞에 0b라는 값이 추가되므로, 해당 문자열은 제거
        s = str(bin(int(Counter(s)['1']))).replace("0b","")
    return [cnt, zeros]