# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge cases
        if len(lists) == 0: return None
        #merge every 2 lists
        while len(lists) > 1:
            #bind every 2 lists
            i = 0
            mergedLists = []
            while i < len(lists):
                first = lists[i]
                second = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge2Lists(first,second))
                i += 2
            lists = mergedLists
        return lists[0]
        #helper func
    def merge2Lists(self, list1, list2):
        res = pr = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                pr.next = list1
                list1 = list1.next
            else:
                pr.next = list2
                list2 = list2.next
            pr = pr.next
        pr.next = list1 or list2
        return res.next