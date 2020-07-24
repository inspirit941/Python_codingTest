def solution(s: str):
    def expand(left: int, right: int) -> str:
      # 현재 left idx, right idx가 같은 문자열일 경우
      # 윈도우 크기를 좌우로 1씩 넓힌다.
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]
    # 연산 필요없는 경우
    if len(s) < 2 or s == s[::-1]:
        return len(s)
      
    result = ""
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i,i+2), key = len)
    
    return len(result)