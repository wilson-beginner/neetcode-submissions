class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            if num - 1 not in numSet:
                end = num + 1

                while end in numSet:
                    end += 1

                res = max(res, end - num)

        return res