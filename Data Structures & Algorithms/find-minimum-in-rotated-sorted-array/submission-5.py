class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = 5001
        while l <= r:
            #not rotated
            if nums[l] <= nums[r]: return nums[l]
            #rotated
            mid = (l+r) // 2
            res = min(res, nums[mid])
            #mid on bigger side
            if nums[mid] >= nums[l]:
                l = mid+1
            #mid on smaller side
            else:
                r = mid
        return res