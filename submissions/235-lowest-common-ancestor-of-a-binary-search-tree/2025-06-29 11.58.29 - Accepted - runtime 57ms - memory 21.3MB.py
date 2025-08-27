# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lcs(p_path, q_path):
            lcs = None
            for p, q in zip(p_path, q_path):
                if p.val == q.val:
                    lcs = p
            return lcs

        def dfs(root, node, path, found):
            if not root:
                return path, False
            path.append(root)
            if root.val == node.val:
                found = True
            elif node.val < root.val:
                path, found = dfs(root.left, node, path, found)
            else:
                path, found = dfs(root.right, node, path, found)
            if not found:
                path.pop(-1)
            return path, found

        p_path, _ = dfs(root, p, [], False)
        q_path, _ = dfs(root, q, [], False)
        
        # p_path = [n.val for n in p_path]
        # q_path = [n.val for n in q_path]
        # print(p_path, q_path)
        return lcs(p_path, q_path) 
        