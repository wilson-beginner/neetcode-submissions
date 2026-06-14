class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        #turn each string into a tuple (list first)
        for string in strs:
            alpha = [0] * 26
            for c in string:
                alpha[ord(c)-ord('a')] += 1
            ans[tuple(alpha)].append(string)
        return [group for group in ans.values()]