class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1]*size
        suffix = [1]*size
        for i in range(1,size):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[size-1-i] = suffix[size-i]*nums[size-i]
        return [p*s for p, s in zip(prefix,suffix)]
