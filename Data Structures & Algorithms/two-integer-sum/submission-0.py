class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for idx in range(len(nums)):
            if nums[idx] in map:
                return [min(map[nums[idx]], idx), max(map[nums[idx]], idx)]
            map[nums[idx]] = idx;
            map[target-nums[idx]] = idx;
        return []