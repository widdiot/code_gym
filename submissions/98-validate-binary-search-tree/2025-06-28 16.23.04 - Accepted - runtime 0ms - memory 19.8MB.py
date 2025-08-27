# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, mini, maxi):
            if not node:
                return True
            left = dfs(node.left, mini, node.val)
            right = dfs(node.right, node.val, maxi)
            curr = node.val > mini and node.val < maxi
            return curr and left and right
        return dfs(root, -2**31 - 1, 2**31)
        