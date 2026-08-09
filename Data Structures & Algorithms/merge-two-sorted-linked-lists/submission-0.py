# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        pr = res
        p1, p2 = list1, list2
        while p1 != None and p2 != None:
            temp = ListNode()
            if p1.val <= p2.val:
                temp.val = p1.val
                p1 = p1.next
            else:
                temp.val = p2.val
                p2 = p2.next
            pr.next = temp
            pr = pr.next
        if p1 != None:
            pr.next = p1
        else:
            pr.next = p2
        return res.next