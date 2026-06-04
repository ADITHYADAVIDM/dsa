class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            l.append(product)
        return l

example = Solution()
print(example.productExceptSelf([1,2,3,4]))