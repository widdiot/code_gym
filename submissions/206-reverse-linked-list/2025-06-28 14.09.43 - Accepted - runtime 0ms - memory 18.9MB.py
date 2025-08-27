# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        def dfs(node, prev):
            nonlocal new_head
            if not node: 
                return 
            new_head = node
            dfs(node.next, node)
            node.next = prev
            return
        dfs(head, None)
        return new_head