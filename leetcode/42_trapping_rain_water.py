class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        result = 0
        # 왼쪽 / 오른쪽의 idx 지정
        left, right = 0, len(height)-1
        # 왼쪽 / 오른쪽의 최고높이 결정
        left_height, right_height = height[left], height[right]
        
        while left < right:
          # 현재 위치 기준으로 왼쪽 / 오른쪽 높이 최댓값 경신
            left_height, right_height = max(left_height, height[left]), max(right_height, height[right])
            # left 높이가 right보다 작거나 같을 경우 left idx 이동
            if left_height <= right_height:
                result += left_height - height[left]
                left += 1
            else:
              # right idx 이동
                result += right_height - height[right]
                right -= 1
        return result