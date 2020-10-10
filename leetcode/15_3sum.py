class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        # 가장 작은 값을 고정하고, 중간값과 큰 값을 투 포인터로 계산한다.
        # 고정값 index = start.
        for start in range(len(nums) - 2):
            # 한 번 고정값으로 사용했다면 건너뛴다.
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            
            # 투 포인터로 간격을 줄여가며 합 계산
            left, right = start+1, len(nums) - 1
            while left < right:
                sums = nums[start] + nums[left] + nums[right]
                # 0보다 작으면 left 위치를, 0보다 크면 right 위치를 이동시킨다.
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    answer.append([nums[start], nums[left], nums[right]])
                    # 중복연산 제거를 위해 left, right값 추가이동
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer