class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 겹치는 구간파악을 위해, 먼저 정렬
        merged = []
        for arr in sorted(intervals, key = lambda x: x[0]):
            # arr의 시작점이 구간 안에 있는 경우
            if merged and arr[0] <= merged[-1][1]:
                # arr의 끝점과 merged 끝점 중 더 긴 것을 merged 끝점에 업데이트
                merged[-1][1] = max(merged[-1][1], arr[1])
            else:
                merged += arr,
                # a = [1]
                # b = [2,3]
                # a += b // returns [1,2,3]
                # a += b, // returns [1, [2,3]]. a += [b]와 동일한 결과를 리턴한다.
        return merged