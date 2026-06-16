class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        start = 0
        i = 0
        sList = []
        while start < len(s):
            if(s[start+i] == "#"):
                size = int(s[start:start+i])
                if(size > 0):
                    sList.append(s[start+i+1:start+i+1+size])
                else:
                    sList.append("")
                start += (i+1+size)
                i = 0
            i += 1
        return sList

# strs: [], return ''
# strs: [""], res = [0, #, ""], return '0#'

# 0 1 2 3 4 5 6 7 8 9 10
# 4 # a b f d 3 # h t r
