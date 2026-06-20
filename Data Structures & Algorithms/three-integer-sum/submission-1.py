class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        res = []
        for i1 in range(len(numbers)-2):
            # fixed index dup
            if i1 > 0 and numbers[i1]==numbers[i1-1]:
                continue
            # pairs dup
            L = i1+1
            R = len(numbers)-1
            while L < R:
                twoSum = numbers[L]+numbers[R]
                if twoSum == -numbers[i1]:
                    res.append([numbers[i1], numbers[L], numbers[R]])
                    L += 1
                    R -= 1
                    while L < R and numbers[L] == numbers[L-1]:
                        L += 1
                    while L < R and numbers[R] == numbers[R+1]:
                        R -= 1
                elif twoSum > -numbers[i1]:
                    R -= 1
                else:
                    L += 1
        return res

