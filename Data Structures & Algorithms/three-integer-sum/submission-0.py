class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        twoSum = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i > j):
                    twoSum[nums[i]+nums[j]].append((i,j))
        res = []
        had = []
        for i in range(len(nums)):
            compliment = -nums[i]
            exists = twoSum[compliment]
            for t in exists:
                if i not in t and set([nums[i],nums[t[0]],nums[t[1]]]) not in had:
                    res.append([nums[i],nums[t[0]],nums[t[1]]])
                    had.append(set([nums[i],nums[t[0]],nums[t[1]]]))
        return res