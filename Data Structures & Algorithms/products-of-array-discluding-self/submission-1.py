class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1]*size
        for i in range(1,size):
            ans[i] = ans[i-1]*nums[i-1]
        suffix = 1
        for i in range(size-1, -1, -1): 
            ans[i] *= suffix
            suffix *= nums[i]
        return ans