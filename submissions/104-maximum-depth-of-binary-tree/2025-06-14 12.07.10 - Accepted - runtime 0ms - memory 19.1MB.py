# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(root, depth):
            if not root:
                return depth
            depth += 1
            left_depth = dfs(root.left, depth)
            right_depth = dfs(root.right, depth)
            return max(left_depth, right_depth)
        return dfs(root, depth)

        