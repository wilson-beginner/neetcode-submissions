class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre, post = 1, 1
        for i in range(1,len(nums)):
            pre *= nums[i-1]
            ans[i] *= pre
        for i in range(len(nums)-2,-1,-1):
            post *= nums[i+1]
            ans[i] *= post
        return ans