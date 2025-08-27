# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def delete(head, node, prev):
            if not prev:
                return head.next
            elif node.next:
                prev.next = node.next
                return head
            else:
                prev.next = None
                return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        k = length - n

        node = head
        idx = 0
        prev = None
        while node:
            if idx == k:
                head = delete(head, node, prev)
                break
            idx += 1
            prev = node
            node = node.next

        return head

        