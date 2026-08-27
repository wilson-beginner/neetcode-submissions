# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            l_max = dfs(root.left)+root.left.val if root.left else 0
            r_max = dfs(root.right)+root.right.val if root.right else 0
            l_max = max(l_max, 0)
            r_max = max(r_max, 0)
            res[0] = max(res[0], l_max+r_max+root.val)
            return max(l_max, r_max)
        dfs(root)
        return res[0]