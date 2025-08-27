# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Optimal
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        first_even = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = first_even
        return head
            
