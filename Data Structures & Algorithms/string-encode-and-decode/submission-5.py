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
        sList = []

        while start < len(s):
            i = 0

            while s[start + i] != "#":
                i += 1

            size = int(s[start:start+i])
            content_start = start + i + 1

            sList.append(s[content_start:content_start+size])

            start = content_start + size

        return sList