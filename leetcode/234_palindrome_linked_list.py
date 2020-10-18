# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        # deque를 활용한 풀이
        # 링크드 리스트 데이터를 deque에 저장.
        queue: Deque = deque()
        node = head
        while node:
            queue.append(node.val)
            node = node.next
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True
            
        