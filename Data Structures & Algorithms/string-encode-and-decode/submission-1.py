class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeList = ""
        for string in strs:
            encodeList += str(len(string)).zfill(3)
            encodeList += string
        return encodeList

    # strs: [""], eL: "000"
    # strs: [], eL: ""

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        start = 0
        stringList = []
        while(start < len(s)):
            size = int(s[start:start+3])
            # if (size == 0):
            #     stringToAdd = ""
            # else:
            #     stringToAdd = str[start+3:start+3+size]
            stringList.append(""+s[start+3:start+3+size])
            start += (3+size)
        return stringList
        # return [""] if len(stringList) == 0 else stringList

        # 0 1 2 3  4
        # 0 0 0 "" 

        # 0 1 2 3 4 5 6 7 8 9 10 11
        # 0 0 2 a b 0 0 4 f e w  g