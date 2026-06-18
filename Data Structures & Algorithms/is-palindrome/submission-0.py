class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for string in s:
            if (ord('Z') >= ord(string) >= ord('A')) or (ord('z') >= ord(string) >= ord('a')) or (ord('9') >= ord(string) >= ord('0')):
                ls.append(string.lower())
        s2 = ''.join(ls)

        R = len(s2) - 1
        for L in range(0, len(s2)//2):
            if(s2[L] != s2[R]): return False
            R -= 1
        return True
