class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:return 0
        l, r=0,1
        sub = set()
        sub.add(s[l])
        res = 1
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                res=max(res,r-l+1)
                r+=1
            else:
                while(s[l] != s[r]):
                    sub.remove(s[l])
                    l+=1
                sub.remove(s[l])
                l+=1
        return res
        
# abca
# 3. Psuedocode
#     1. 用L和R控制substring，set去維持目前substring的char，res紀錄最大長度
#     2. R會掃過string一遍，並且看是否重複
#         1. 若R沒重複 ⇒ R被加入substring，R右移
#         2. 若R重複 ⇒ 代表目前有兩個一樣char，一個在substring內，一個欲加入。
#         ⇒ L右移，直到找到一樣的char，同時右移路徑上的char都要移除set，R的char加入
#         ⇒ R重複了代表目前這個substring的長度不會再長，要跟res比較