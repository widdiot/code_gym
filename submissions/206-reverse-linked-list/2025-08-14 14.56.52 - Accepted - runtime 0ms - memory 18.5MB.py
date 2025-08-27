# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        node = head
        while node:
            node.val = stack.pop()
            node = node.next
        return head