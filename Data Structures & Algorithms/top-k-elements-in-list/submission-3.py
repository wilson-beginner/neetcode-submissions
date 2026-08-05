class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range (len(nums)+1)]
        hashMap = {}
        res = []
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        for key, value in hashMap.items():
            freq[value].append(key)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k: return res

            