class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 부분 문자열. 연속된 문자열이어야 한다.
        # 슬라이딩 윈도우 + 투 포인터로 사이즈 조절하기
        start, end, max_len = 0, 0, 0
        # 이미 존재하는 String -> index 기록
        exists = dict()
        for idx, char in enumerate(s):
            # 이미 있는 문자열이고, 현재 윈도우 시작위치가 해당 문자열 등장위치보다 이전일 경우
            # window의 시작지점을 해당 문자열 위치 다음으로 옮긴다.
            if char in exists and start <= exists[char]:
                start = exists[char] + 1
            else: # 최대 문자열의 길이를 구한다
                max_len = max(max_len, idx - start + 1)
            # 현재 문자열의 위치 업데이트
            exists[char] = idx
        return max_len
                