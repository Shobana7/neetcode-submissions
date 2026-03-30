# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None
        idx_map = {}
        for i, v in enumerate(inorder):
            idx_map[v] = i
        
        self.pre_idx = 0

        def dfs(l,r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            
            root_idx = idx_map[preorder[self.pre_idx]]
            self.pre_idx += 1
            root.left = dfs(l,root_idx-1)
            root.right = dfs(root_idx + 1,r)

            return root

        return dfs(0, len(inorder)-1)