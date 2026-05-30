# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        nxt = second.next
        second.next = None

        while nxt:
            tmp = nxt.next
            nxt.next = second
            second = nxt
            nxt = tmp
        

        curr = head

        while curr and second:
            t = curr.next
            t2 = second.next
            curr.next = second
            second.next = t
            curr = t
            second = t2






