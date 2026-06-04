class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        l = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t < 0:
                    j += 1
                elif t > 0:
                    k -= 1
                else:
                    l.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return l

example = Solution()
print(example.threeSum([-1,0,1,2,-1,-4]))