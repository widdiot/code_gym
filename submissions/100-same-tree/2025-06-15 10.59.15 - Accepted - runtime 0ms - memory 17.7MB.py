# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            # xor
            if (not a and b) or (a and not b):
                return False
            elif not a and not b:
                return True
            curr = a.val == b.val
            left, right = dfs(a.left, b.left), dfs(a.right, b.right)
            return curr and left and right
        return dfs(p,q)
        