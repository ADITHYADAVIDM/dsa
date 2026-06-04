class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [None] * n
        product = 1
        for i in range(n):
            l[i] = product
            product *= nums[i]
        product = 1
        for i in range(n):
            l[n - 1 - i] *= product
            product *= nums[n - 1 - i]
        return l

example = Solution()
print(example.productExceptSelf([1,2,3,4]))