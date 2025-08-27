# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            lheight, rheight = dfs(root.left), dfs(root.right)
            curr_dia = lheight + rheight
            diameter = curr_dia if curr_dia > diameter else diameter
            height = lheight if lheight > rheight else rheight
            return height + 1
        dfs(root)
        return diameter
            
            
        