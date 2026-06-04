class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for num in range(len(nums)):
            comp = target - nums[num]
            if comp in seen:
                return [seen[comp], num]
            else:
                seen[nums[num]] = num
        return None

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))