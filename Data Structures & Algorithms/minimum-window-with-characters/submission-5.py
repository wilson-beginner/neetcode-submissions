from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        l = 0
        minLen = float("inf")
        minSub = ""

        for r in range(len(s)):
            if s[r] in need:
                if need[s[r]] > 0:
                    missing -= 1
                need[s[r]] -= 1

            while missing == 0:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minSub = s[l:r+1]

                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        missing += 1

                l += 1

        return minSub