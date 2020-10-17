import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 최솟값을 매번 갱신하면서
        # 현재 값과 최솟값과의 차이를 구해 최댓값을 저장하도로 한다
        # 카데인(Kadane) 알고리즘으로, O(n) 에 풀이 가능
        profit = 0
        min_price = math.inf
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit