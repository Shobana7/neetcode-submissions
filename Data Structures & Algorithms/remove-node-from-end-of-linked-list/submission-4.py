# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        s,f = head, head

        for i in range(n):
            f = f.next
            if not f:
                return head.next
        
        while f and f.next:
            s = s.next
            f = f.next
        
        s.next = s.next.next

        return head