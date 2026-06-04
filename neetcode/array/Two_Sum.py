class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}
        for i, j in enumerate(nums):
            look_up[i] = j
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                for index, number in look_up.items():
                    if nums[i] == number:
                        u = index
                        break
                for index, number in look_up.items():
                    if nums[j] == number and u != index:
                        v = index
                        break
                x = [u, v] if u < v else [v, u]
                return x
        return None

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))