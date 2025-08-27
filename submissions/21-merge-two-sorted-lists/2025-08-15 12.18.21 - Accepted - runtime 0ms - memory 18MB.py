# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        node1, node2 = list1, list2
        head = ListNode()
        res = head
        while node1 or node2:
            if not node1:
                res.next = ListNode(node2.val)
                res = res.next
                node2 = node2.next
            elif not node2:
                res.next = ListNode(node1.val)
                res = res.next
                node1 = node1.next
            else:
                if node1.val <= node2.val:
                    res.next = ListNode(node1.val)
                    res = res.next
                    node1 = node1.next
                else:
                    res.next = ListNode(node2.val)
                    res = res.next
                    node2 = node2.next
        return head.next
        