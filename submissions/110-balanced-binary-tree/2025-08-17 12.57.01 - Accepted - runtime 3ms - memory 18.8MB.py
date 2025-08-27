# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            if not root:
                return 0
            lheight, rheight = dfs(root.left), dfs(root.right)
            if abs(rheight - lheight) > 1:
                balanced = False
            height = lheight if lheight > rheight else rheight
            return height + 1
        dfs(root)
        return balanced
        
        