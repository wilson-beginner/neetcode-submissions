# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            res.append(root)
            if not root: return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        for i in range(len(res)):
            if not res[i]:
                res[i] = "#"
            else:
                res[i] = str(res[i].val)
        res = ",".join(res)
        print(res)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        form = []
        #read str reversely
        for i in range(len(data)-1, -1, -1):
            if data[i] == "#":
                form.append(None)
            else:
                left = form.pop()
                right = form.pop()
                form.append(TreeNode(int(data[i]), left, right))
        return form[0]                    

