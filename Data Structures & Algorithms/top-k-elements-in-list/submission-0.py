class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Iterate the list once, record the frequences of each num ⇒ O(n)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # sort the freq ⇒ O(m*logm), where m is number of distinct elements in nums.
        freq = sorted(freq.items(), key= lambda x: x[1], reverse=True)
        # select top k ⇒ O(k)
        return list(pair[0] for pair in freq[0:k])
        