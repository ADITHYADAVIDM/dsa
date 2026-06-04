class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        l = sorted(freq.items(), key = lambda x: x[1])
        return [i[0] for i in l[-k:]]

example = Solution()
print(example.topKFrequent([1,1,1,2,2,3], 2))