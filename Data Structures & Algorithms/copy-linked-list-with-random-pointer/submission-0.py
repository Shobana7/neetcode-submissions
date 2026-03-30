"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        mapping = {}

        node = head
        while node:
            newNode = Node(x=node.val)
            mapping[node] = newNode
            node = node.next
        
        node = head
        while node:
            mapping[node].next = mapping[node.next] if node.next else None
            mapping[node].random = mapping[node.random] if node.random else None
            node = node.next
        
        return mapping[head]

