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
            else:
                prev.next = node.next
                return head
        count = 0
        node = head
        while count < n:
            node = node.next
            count += 1

        node2 = head
        prev = None
        while node:
            prev = node2
            node2 = node2.next
            node = node.next
        
        return delete(head, node2, prev)

        