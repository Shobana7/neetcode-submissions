# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ptrs = [None]*len(lists)
        for i, h in enumerate(lists):
            ptrs[i] = h

        res = ListNode()
        dummy = res
        

        while True:
            idx_won = 0
            min_this_round = 20000
            all_none = 0
            print(ptrs)
            for i in range(len(ptrs)):
                if not ptrs[i]:
                    all_none += 1
                    continue
                if ptrs[i].val <= min_this_round:
                    idx_won = i
                    min_this_round = ptrs[i].val
            if all_none == len(lists):
                break
            res.next = ListNode(min_this_round)
            res = res.next
            ptrs[idx_won] = ptrs[idx_won].next
            print(idx_won, min_this_round)
        
        return dummy.next

        
            

            