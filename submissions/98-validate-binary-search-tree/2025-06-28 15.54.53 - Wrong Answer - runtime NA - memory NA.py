# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            curr_l = node.left.val < node.val if node.left else True
            curr_r = node.right.val > node.val if node.right else True
            curr = curr_l and curr_r
            left, right = dfs(node.left), dfs(node.right)
            return curr and left and right
        return dfs(root)
        