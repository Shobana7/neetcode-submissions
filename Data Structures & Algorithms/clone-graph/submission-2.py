"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_mapping = {}

        def dfs(n):
            if not n:
                return None
            
            if n in node_mapping:
                return node_mapping[n]
            
            node_mapping[n] = Node(n.val)
            for neigh in n.neighbors:
                node_mapping[n].neighbors.append(dfs(neigh))
            return node_mapping[n]
        
        return dfs(node)