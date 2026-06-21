# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        s,f = head,head

        while f and n:
            f = f.next
            n -= 1
        
        if n:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while f:
            prev = prev.next
            s,f = s.next, f.next
    

        prev.next = prev.next.next

        return dummy.next