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
        
        root = TreeNode(preorder[0])
        root_idx = idx_map[preorder[0]]
        left = inorder[:root_idx]
        right = inorder[root_idx+1:]

        print(left, right)
        print(preorder[1:len(left)+1])
        print(preorder[len(left)+1:])

        root.left = self.buildTree(preorder[1:len(left)+1], left)
        root.right = self.buildTree(preorder[len(left)+1:], right)

        return root