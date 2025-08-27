# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def attach_at_end(node1, node2):
            if not node1:
                return
            if not node1.right:
                node1.right = node2
            else:
                attach_at_end(node1.right, node2)
            return

        def dfs(node, key, parent):
            if not node:
                return
            if key == node.val:
                if parent:
                    if node.left and node.right:
                        parent.left = node.left
                        attach_at_end(node.left, node.right)
                    else:
                        parent.left = node.left
            elif key < node.val:
                dfs(node.left, key, node)
            else:
                dfs(node.right, key, node)
            return
        dfs(root, key, None)
        return root