class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            #not rotated
            if nums[r] >= nums[l]:
                if target < nums[mid]:
                    r=mid-1
                elif target == nums[mid]:
                    return mid
                else:
                    l=mid+1
            #rotated
            else:
            #mid on bigger side
                if nums[mid] >= nums[l]:
                    #3 conditions
                    if target > nums[mid]:
                        l = mid+1
                    elif target == nums[mid]:
                        return mid
                    else:
                        if target >= nums[l]:
                            r = mid - 1
                        else:
                            l = mid + 1
                else:
                    #3 conditions
                    if target < nums[mid]:
                        r=mid-1
                    elif target == nums[mid]:
                        return mid
                    else:
                        if target >= nums[l]:
                            r=mid-1
                        else:
                            l = mid + 1
        return -1