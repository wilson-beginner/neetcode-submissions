class Solution:
    def minWindow(self, s: str, t: str) -> str:
        L = 0
        res, resLen = [L,0], float('inf')
        have, need = {}, {}
        for c in t:
            need[c] = need.get(c,0)+1
        con = 0
        for R in range(len(s)):
            #not sat, add R char into have
            if s[R] in need:
                have[s[R]] = have.get(s[R], 0)+1
                #after adding, check sat con num
                if have[s[R]] == need[s[R]]:
                    con += 1
            #sat, removing L char from have
            while con == len(need):
                #compare min res
                if R-L+1 < resLen:
                    resLen = R-L+1 
                    res = [L, R]
                #removing L char 
                if s[L] in need:
                    have[s[L]] -= 1
                    #check if its still sat
                    if have[s[L]] < need[s[L]]:
                        con -= 1
                L += 1
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""