class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        charMap = dict()
        for r in range(0, len(s)):
            charMap[s[r]] = charMap.get(s[r],0)+1
            while r-l+1 - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


# 1. R從左掃到右
# 2. R加入windows
# 3. 若不合法，修正
# 4. 比較長度