# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_smallest(node):
            if not node.left:
                return node.val
            return find_smallest(node.left)

        def dfs(node, key):
            if not node:
                return node
            print(node.val)
            if key == node.val:
                if node.left and node.right:
                    mini = find_smallest(node.right)
                    node.val = mini
                    node.right = dfs(node.right, mini)
                    
                elif node.left:
                    return node.left
                else:
                    return node.right
            elif key < node.val:
                left = dfs(node.left, key)
                node.left = left
            else:
                right = dfs(node.right, key)
                node.right = right
            return node
        
        return dfs(root, key)