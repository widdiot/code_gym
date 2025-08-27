# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def dfs(root, sol):
            if root == None:
                return
            sol.append(root.val)
            dfs(root.left, sol)
            dfs(root.right, sol)
            return
        dfs(root, sol)
        return sol