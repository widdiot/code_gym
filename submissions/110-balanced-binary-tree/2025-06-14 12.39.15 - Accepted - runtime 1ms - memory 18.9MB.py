# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            left_depth, left_balanced = dfs(root.left)
            right_depth, right_balanced = dfs(root.right)
            balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
            return 1+max(left_depth, right_depth), balanced
        _, balanced = dfs(root)
        return balanced
        
        