class Solution:
    def climbStairs(self, n: int) -> int:
        base1, base2 = 1, 1
        cur = base1
        for i in range(n-1):
            cur = base1+base2
            base1=base2
            base2=cur
        return cur