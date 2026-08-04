class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            if c in hashMap:
                if not stack or stack[-1] != hashMap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False