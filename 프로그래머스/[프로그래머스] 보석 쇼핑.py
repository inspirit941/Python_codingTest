from collections import defaultdict
import heapq
def solution(gems):
    start, end = 0, 1
    gem_loc = defaultdict(int)
    gem_target = len(set(gems))
    
    # 가장 길이가 짧은 좌표 저장을 위해 heap 자료구조 사용.
    answer = []
    
    # 첫 번째 보석의 위치.
    gem_loc[gems[start]] = 1
    
    while start < len(gems):
        if len(gem_loc) == gem_target:
            heapq.heappush(answer, (end - start + 1, start, end))
            # start를 오른쪽으로 이동
            # 현재 start 위치의 값을 1 낮춘다.
            # 0이 될 경우, 해당 보석이 범위 내에 없게 된다.
            gem_loc[gems[start]] -= 1
            if gem_loc[gems[start]] == 0:
                # 보석 삭제
                del gem_loc[gems[start]]
            start += 1
        else:
            ## 더 이상 포인터 이동이 불가능.
            if end == len(gems):
                break
            gem_loc[gems[end]] += 1
            end += 1
    
    return [answer[0][1]+1, answer[0][2]]