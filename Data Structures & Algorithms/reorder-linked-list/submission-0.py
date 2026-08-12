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
        #find last node of L half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #start node of R half
        R = slow.next
        #reverse R half
        prev = None
        while R:
            temp = R.next
            R.next = prev
            prev = R
            R = temp
        R = prev
        #last node of L point to None
        slow.next = None
        #alt taking both node
        L = head
        while L:
            templ = L.next
            L.next = R
            L = templ
            if R:
                tempr = R.next
                R.next = L
                R = tempr
