"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        node_mapping = {}

        def dfs(currnode):
            if not currnode:
                return None
        
            if currnode in node_mapping:
                return node_mapping[currnode]

            node_mapping[currnode] = Node(currnode.val)
            for n in currnode.neighbors:
                node_mapping[currnode].neighbors.append(dfs(n))
            return node_mapping[currnode]
        
        return dfs(node)


