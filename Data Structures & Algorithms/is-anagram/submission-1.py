class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = defaultdict(int)
        for sChar, tChar in zip(s,t):
            ana[sChar] += 1
            ana[tChar] -= 1
        return not any (val!= 0 for val in ana.values())