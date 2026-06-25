class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        sub = set()
        for r in range(len(s)):
            #檢查重複
            while(s[r] in sub):
                sub.remove(s[l])
                l+=1
            #執行不重複    
            sub.add(s[r])
            res=max(res,r-l+1)
        return res
        
             