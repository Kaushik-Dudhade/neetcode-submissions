# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        start = head

        while head:
            n+= 1
            head = head.next

        mid = n //2

        cur = start

        while mid:
            cur = cur.next
            mid -= 1
        
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        
        end = prev

        cur = ListNode()
      

        for i in range(n):
            if i%2 == 0:
                cur.next = start
                start = start.next
                cur = cur.next
            else:
                cur.next = end
                end = end.next
                cur = cur.next
        
        return cur.next













