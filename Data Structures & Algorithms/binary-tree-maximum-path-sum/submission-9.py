class Solution:
    def maxPathSum(self, root):
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            l_max = max(dfs(root.left), 0)
            r_max = max(dfs(root.right), 0)
            res[0] = max(res[0], l_max+r_max+root.val)
            return max(l_max, r_max)+root.val
        dfs(root)
        return res[0]