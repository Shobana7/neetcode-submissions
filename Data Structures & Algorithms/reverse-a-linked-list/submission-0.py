# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        nextNode = head.next
        head.next = None

        while nextNode:
            temp = nextNode.next
            nextNode.next = head
            head = nextNode
            nextNode = temp
        
        return head