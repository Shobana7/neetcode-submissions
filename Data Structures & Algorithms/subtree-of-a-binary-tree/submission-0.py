# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.startNode = False
        def dfs(node):
            if not node:
                return 
            
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                self.startNode = True
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return self.startNode
            
                
        
        
        
