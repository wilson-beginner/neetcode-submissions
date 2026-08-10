# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        toBeAdded = [root]
        stack = []
        depth = 0
        while toBeAdded:
            while toBeAdded:
                node = toBeAdded.pop()
                stack.append(node)
            if stack: depth += 1
            while stack:
                node = stack.pop()
                if node.left: toBeAdded.append(node.left)
                if node.right: toBeAdded.append(node.right)
        return depth