# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lnode = None
        rnode = head
        l, r = 0, 0
        while rnode:
            rnode = rnode.next
            r += 1
            if r > n:
                l += 1
                if not lnode:
                    lnode = head
                else:
                    lnode = lnode.next
            if not rnode:
                if not lnode:
                    head = head.next
                else:
                    lnode.next = lnode.next.next
        return head
                
