# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        #let fast go first
        for i in range(0,2):
            if fast:
                fast = fast.next
        #fast hasnt reached None
        while fast != None:
            #fast meet slow means cycle
            if fast == slow:
                return True
            #fast move twice
            for i in range(0,2):
                if fast:
                    fast = fast.next
            #slow move once
            slow = slow.next
        return False