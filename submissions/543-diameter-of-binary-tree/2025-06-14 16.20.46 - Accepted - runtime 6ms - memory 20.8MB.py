# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(node):
            nonlocal d
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            h = max(left, right)
            d = max(left + right, d)
            return 1 + h
        h = dfs(root)
        return d
            
        