# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        curr = head
        nxtNode = head.next
        curr.next = None

        while nxtNode:
            temp = nxtNode.next
            nxtNode.next = curr
            curr = nxtNode
            nxtNode = temp
        
        return curr

