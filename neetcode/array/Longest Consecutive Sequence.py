class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = set(nums)
        max_count = float('-inf')
        for num in unique:
            if num - 1 not in unique:
                count = 1
                num1 = num
                while num1 +  1 in unique:
                    num1 += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count

example = Solution()
print(example.longestConsecutive([100, 4, 200, 1, 3, 2]))