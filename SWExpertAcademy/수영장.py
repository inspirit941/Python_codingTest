def dfs(idx, price):
    global answer
    if idx >= len(days):
        answer = min(answer, price)
        return
    # 1일 이용권 결제
    if days[idx] == 0:
        dfs(idx+1, price)
    else:
        dfs(idx+1, price + (days[idx] * prices[0]))
        # 1개월 이용권 결제
        dfs(idx+1, price + prices[1])
        # 3개월 이용권 결제
        dfs(idx+3, price + prices[2])
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  
    prices = list(map(int,input().split()))
    days = list(map(int,input().split()))
    # 초기값 = 1년 이용권 사용
    answer = prices[-1]
    dfs(0, 0)
    print("#{} {}".format(test_case, answer))
	
    