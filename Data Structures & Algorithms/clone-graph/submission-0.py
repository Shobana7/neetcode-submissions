"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mapping = {}

        def dfs(start):      
            if not start:
                return None

            if start in mapping:
                return mapping[start]

            mapping[start] = Node(start.val)

            for neighbor in start.neighbors:
                mapping[start].neighbors.append(dfs(neighbor))
            return mapping[start]
        
        return dfs(node)



            