class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)): 
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            L, R = idx+1, len(nums)-1
            while L < R:
                threeSum = nums[L]+nums[R]+nums[idx]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([nums[idx], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L]==nums[L-1]:
                        L += 1
        return res