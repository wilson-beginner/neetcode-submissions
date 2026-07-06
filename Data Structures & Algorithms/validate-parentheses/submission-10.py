class Solution:
    def isValid(self, s: str) -> bool:
        paraMatch = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack=[]
        for char in s:
            if char in paraMatch:
                if stack:
                    top = stack.pop()
                    if paraMatch[char] != top:
                        return False
                else: return False
            else:
                stack.append(char)
        return True if not stack else False
