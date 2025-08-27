# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            depth += 1
            ldepth = dfs(root.left, depth)
            rdepth = dfs(root.right, depth)
            depth = ldepth if ldepth > rdepth else rdepth
            return depth
        depth = dfs(root, 0)
        return depth
            


        