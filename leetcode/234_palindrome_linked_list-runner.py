# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Runner 활용한 풀이
        # 두칸씩 이동하는 fast, 한칸씩 이동하는 slow를 정의하면
        # fast가 끝까지 도착하면 slow는 절반의 위치에 도달한다.
        
        # slow로 지나온 노드를 역순으로 rev에 저장하고
        # 절반의 지점에서부터 slow가 끝까지 도달할 때까지
        # slow와 rev 값을 비교한다.
        
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 만약 전체 노드 길이가 홀수라면, fast.next는 None인데 fast는 not None이다. 두 칸씩 건너뛰기 때문.
        if fast:
            slow = slow.next
        # slow와 rev 값 비교
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        # 끝까지 도착했으면 rev는 None일테니 not rev는 True.
        return not rev