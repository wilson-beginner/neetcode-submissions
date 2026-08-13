# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case
        if not root and not subRoot:
            return True
        elif root and subRoot:
            return self.isSametree(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else: return False
    #helper function
    def isSametree(self, t1, t2):
        #base case
        if not t1 and not t2:
            return True
        elif t1 and t2:
            if t1.val != t2.val: return False
            return self.isSametree(t1.left, t2.left) and self.isSametree(t1.right, t2.right)
        else: return False
