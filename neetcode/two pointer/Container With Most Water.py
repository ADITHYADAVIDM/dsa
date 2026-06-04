class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        max_cap = float('-inf')
        while i < j:
            max_cap = max(max_cap, (j - i) * min(heights[i], heights[j]))
            if heights[i] > heights[j]:
                j -= 1
            elif i < j:
                i += 1
            else:
                i += 1
                j -= 1
        return max_cap

example = Solution()
print(example.maxArea([1,8,6,2,5,4,8,3,7]))