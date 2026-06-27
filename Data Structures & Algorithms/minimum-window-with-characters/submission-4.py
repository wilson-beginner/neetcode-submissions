class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needMap = dict(Counter(t))
        minLen=1001
        minSub=""
        l=0
        #R最終會看所有s char
        for r in range(len(s)):
            if s[r] in needMap: needMap[s[r]] -= 1
            #合法
            if all(v <= 0 for v in needMap.values()):
                #L向右直到不合法
                while all(v <= 0 for v in needMap.values()):
                    if s[l] in needMap:
                        needMap[s[l]]+=1
                    l+=1
                #比較更新
                if r-(l-1)+1 < minLen: 
                    minLen = r-(l-1)+1
                    minSub = s[l-1:r+1]
        return minSub