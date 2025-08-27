# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if not a:
                return False
            if self.isSameTree(a, b):
                return True
            return dfs(a.left, b) or dfs(a.right, b)
        return dfs(root, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return dfs(a.left, b.left) and dfs(a.right, b.right)
            return False
        return dfs(p,q)