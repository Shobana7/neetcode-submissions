# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.mxDepth = 1

        def dfs(node,d):
            if not node:
                return

            self.mxDepth = max(self.mxDepth, d)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 1)
        return self.mxDepth
            
