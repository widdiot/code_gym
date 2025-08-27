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
        def split(head):
            slow = head
            fast = head
            prev = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow
        
        def reverse(head):
            node = head
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        def merge(ptr1, ptr2):
            head = ptr1
            while ptr1 and ptr2:
                nxt1, nxt2 = ptr1.next, ptr2.next
                ptr1.next = ptr2
                if not nxt1:
                    break
                ptr2.next = nxt1
                ptr1, ptr2 = nxt1, nxt2      
        
        mid = split(head)
        rev = reverse(mid)
        merge(head, rev)
        return head



