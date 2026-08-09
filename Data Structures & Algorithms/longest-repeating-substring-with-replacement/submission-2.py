class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = [0] * 26
        L = 0
        res = 0
        for R in range(len(s)):
            maxf = -1
            charMap[ord(s[R])-ord("A")] += 1
            for freq in charMap:
                maxf = max(maxf, freq)
            if R-L+1 - maxf > k:
                charMap[ord(s[L])-ord("A")] -= 1
                L += 1
            else:
                res = max(R-L+1, res)
        return res