class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                end = num+1
                while(end in nums):
                    end += 1
                length = end - num
                if length > res: res = length
        return res