# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def dfs(root, sol):
            if root == None:
                return
            dfs(root.left, sol)
            dfs(root.right, sol)
            sol.append(root.val)
            return
        dfs(root, sol)
        return sol