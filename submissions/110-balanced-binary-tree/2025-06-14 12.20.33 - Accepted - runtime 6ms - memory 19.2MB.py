# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = 0
        def dfs(root, depth, balanced):
            if not root:
                return depth, balanced
            depth += 1
            left_depth, left_balanced = dfs(root.left, depth, balanced)
            right_depth, right_balanced = dfs(root.right, depth, balanced)
            balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
            return max(left_depth, right_depth), balanced
        _, balanced = dfs(root, depth, True)
        return balanced
        
        