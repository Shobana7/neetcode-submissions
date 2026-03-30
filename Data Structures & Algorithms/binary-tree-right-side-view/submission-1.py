# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            x = len(q)
            lastNode = None
            for i in range(x):
                node = q.popleft()
                lastNode = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if lastNode:
                res.append(lastNode.val)

        return res
