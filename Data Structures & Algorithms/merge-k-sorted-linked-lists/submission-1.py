# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        res = ListNode()
        dummy = res
        

        while True:
            idx_won = 0
            min_this_round = 20000
            all_none = 0
            for i in range(len(lists)):
                if not lists[i]:
                    all_none += 1
                    continue
                if lists[i].val <= min_this_round:
                    idx_won = i
                    min_this_round = lists[i].val
            if all_none == len(lists):
                break
            res.next = ListNode(min_this_round)
            res = res.next
            lists[idx_won] = lists[idx_won].next
        
        return dummy.next

        
            

            