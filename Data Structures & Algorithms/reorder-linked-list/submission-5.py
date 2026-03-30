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
            slow = slow.next
            fast = fast.next.next
        
        newHead = slow.next
        slow.next = None

        nextNode = newHead.next
        newHead.next = None

        while nextNode:
            temp = nextNode.next
            nextNode.next = newHead
            newHead = nextNode
            nextNode = temp

        
        curr = head

        while curr and newHead:
            t = curr.next
            temp2 = newHead.next
            curr.next = newHead
            newHead.next = t 
            curr = t
            newHead = temp2
        
        return 