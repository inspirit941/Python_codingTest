class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 트리 구조의 dfs로 해결하기
        result = []
        def dfs(idx, path):
            result.append(path)
            # idx 순서대로 경로를 만들면서 dfs 연산
            for next_idx in range(idx, len(nums)):
                dfs(next_idx + 1, path + [nums[next_idx]])
        
        dfs(0, [])
        return result