# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # split
        right = slow.next
        slow.next = None
        left = head
        # reverse right
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt
        right = prev

        while left and right:
            lnext = left.next
            rnext = right .next
            left.next = right
            right.next = lnext
            right = rnext
            left = lnext
        return head
