# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        prev = None
        node = head
        while node:
            new_head = node
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return new_head
