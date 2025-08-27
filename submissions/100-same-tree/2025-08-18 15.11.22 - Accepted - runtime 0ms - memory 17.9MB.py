# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            curr = p.val == q.val
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return curr and left and right
        else:
            return False
        
        