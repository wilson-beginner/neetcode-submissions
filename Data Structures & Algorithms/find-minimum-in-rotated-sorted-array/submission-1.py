class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[-1] >= nums[0]: return nums[0]
        l, r=0, len(nums)-1
        while(l != r):
            if(nums[r]>nums[l]): return nums[l]
            mid = (l+r)//2
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid
        return nums[l]