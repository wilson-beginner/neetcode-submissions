class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashMap_s, hashMap_t = {}, {}

        for idx in range(len(s)):
            hashMap_s[s[idx]] = hashMap_s.get(s[idx],0)+1
            hashMap_t[t[idx]] = hashMap_t.get(t[idx],0)+1
        
        return hashMap_s == hashMap_t