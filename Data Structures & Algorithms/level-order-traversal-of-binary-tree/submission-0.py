# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res =[]
        queue = deque()
        queue.append(root)
        while queue:
            nextLevel = []
            subRes = []
            while queue:
                out = queue.popleft()
                if out.left: nextLevel.append(out.left)
                if out.right: nextLevel.append(out.right)
                subRes.append(out.val)
            queue.extend(nextLevel)
            res.append(subRes)
        return res


