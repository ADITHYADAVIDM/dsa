class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 1]))
print(solution.hasDuplicate([1, 2, 3, 4]))