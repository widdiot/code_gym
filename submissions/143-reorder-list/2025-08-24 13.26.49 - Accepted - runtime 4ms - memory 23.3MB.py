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
        if not head or not head.next:
            return  # important: avoid single-node self-merge

        def split(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None  # cut only if we actually advanced
            return slow  # start of second half

        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        def merge(ptr1, ptr2):
            while ptr1 and ptr2:
                nxt1, nxt2 = ptr1.next, ptr2.next
                ptr1.next = ptr2
                if not nxt1:      # if first half ended, stop cleanly
                    break
                ptr2.next = nxt1
                ptr1, ptr2 = nxt1, nxt2

        second = split(head)
        second = reverse(second)
        merge(head, second)
        # LeetCode requires in-place; no return needed
