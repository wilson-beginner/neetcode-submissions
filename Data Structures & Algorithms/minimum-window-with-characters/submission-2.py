class Solution:
    def minWindow(self, s: str, t: str) -> str:
        for length in range(len(s)):
            for i in range(len(s)-length):
                isSubstring = True
                curStr = s[i:i+length+1]
                d = dict(Counter(curStr))
                for string in t:
                    if d.get(string,0) == 0:
                        isSubstring = False
                        break
                    else:
                        d[string] -= 1
                if isSubstring:
                    return curStr
        return ""
