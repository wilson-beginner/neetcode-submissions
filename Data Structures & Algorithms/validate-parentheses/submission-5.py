class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False
        char = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                char.append(s[i])
            else:
                if not char: return False
                last = char.pop()
                if not (s[i]==')'and last=='(') and not (s[i]==']'and last=='[') and not (s[i]=='}'and last=="{"):
                    return False
        if char: return False
        return True