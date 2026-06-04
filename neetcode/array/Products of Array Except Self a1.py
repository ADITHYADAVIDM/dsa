class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [None] * n
        prefix = [None] * n
        suffix = [None] * n
        prefix[0] = 1
        suffix[n - 1] = 1
        product = 1
        for i in range(1, n):
            product *= nums[i - 1]
            prefix[i] = product
        product = 1
        for i in range(n - 2, -1, -1):
            product *= nums[i + 1]
            suffix[i] = product
        for i in range(n):
            l[i] = prefix[i] * suffix[i]
        return l
    
example = Solution()
print(example.productExceptSelf([1,2,3,4]))