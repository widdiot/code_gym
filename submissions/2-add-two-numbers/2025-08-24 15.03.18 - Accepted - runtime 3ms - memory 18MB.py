# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while l1 or l2:
            if not l1:
                temp = l2.val+carry
                carry, drop = temp//10, temp%10
                res.next = ListNode(drop)
                res = res.next
                l2 = l2.next
            elif not l2:
                temp = l1.val+carry
                carry, drop = temp//10, temp%10
                res.next = ListNode(drop)
                res = res.next
                l1 = l1.next
            else:
                temp = l1.val + l2.val + carry
                carry, drop = temp//10, temp%10
                res.next = ListNode(drop)
                res = res.next
                l1 = l1.next
                l2 = l2.next
        if carry:
            res.next = ListNode(carry)
        return head.next