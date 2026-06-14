class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create a dict with nums and freq ⇒ O(n)
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        # 2. create different groups that represent the number of freq (bucket sort), length is len(dict)+1
        bucket = [[] for _ in range(max(freq.values())+1) ]
        # 3. put the nums into groups (bucket) according to freq ⇒ O(n)
        for key, value in freq.items():
            bucket[value].append(key)
        # 4. select top k ⇒ O(k)
        ans = []
        count = 0
        for numList in bucket[::-1]:
            for num in numList:
                ans.append(num)
                count += 1
                if(count == k): return ans
        