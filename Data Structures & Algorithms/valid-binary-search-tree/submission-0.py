# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        f, c = float('-inf'), float('inf')
        return self.cmp(root, f, c)

    def cmp(self, cur, f, c):
        if not cur: return True
        return (
            f < cur.val and
            cur.val < c and
            self.cmp(cur.left, f, cur.val) and
            self.cmp(cur.right, cur.val, c)
        )        