class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 현재 온도를 stack에 저장.
        # 다음날 온도가 현재보다 높으면 stack 값을 꺼내서, 날씨차이 저장.
        # 낮으면 스택 값은 계속 유지됨.
        stack = []
        answer = [0 for _ in range(len(T))]
        for idx, value in enumerate(T):
            while stack and value > T[stack[-1]]:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        return answer