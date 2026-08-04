class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            charSet = [0] * 26
            for c in s:
                charSet[ord(c)-ord("a")] += 1
            hashMap[tuple(charSet)].append(s)
        print(hashMap.values())
        return list(hashMap.values())