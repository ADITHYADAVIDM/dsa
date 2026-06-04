class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        def find_water(left, right):
            total = 0
            boundary_min = min(height[left], height[right])
            for i in range(left + 1, right):
                if height[i] > boundary_min:
                    return find_water(left, i) + find_water(i, right)
            total += (right - left - 1) * boundary_min
            for i in range(left + 1, right):
                total -= height[i]
            return total
        n = len(height)
        if n < 3:
            return 0
        i = 0
        j = n - 1
        while i < j and height[i] <= height[i + 1]:
            i += 1
        while i < j and height[j] <= height[j - 1]:
            j -= 1
        left = i
        end = j
        right = left + 1
        while right < end + 1:
            if height[right] >= height[left]:
                total_water += find_water(left, right)
                left = right
                right += 1
            else:
                right += 1
        if height[j] < height[left]:
            total_water += find_water(left, j)
        return total_water

example = Solution()
print(example.trap([4, 1, 3, 1, 2]))