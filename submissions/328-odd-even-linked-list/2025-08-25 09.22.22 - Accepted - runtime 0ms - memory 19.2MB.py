# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#BRUTE FORCE
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        res = []
        while odd:
            if odd:
                res.append(odd.val)
                if odd.next:
                    odd = odd.next.next
                else:
                    break
        while even:
            if even:
                res.append(even.val)
                if even.next:
                    even = even.next.next
                else:
                    break
        node = head
        for i in res:
            node.val = i
            node = node.next
        return head
            
