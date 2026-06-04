class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = {}
        for num in nums:
            if num in count:
                continue
            elif num + 1 in count:
                if num - 1 in count:
                    c = count.get(num - 1) + count.get(num + 1) + 1
                    count[num - count.get(num - 1)] = c
                    count[num + count.get(num + 1)] = c
                    count[num] = c
                else:
                    count[num] = count.get(num + 1) + 1
                    count[num + count.get(num + 1) ] = count[num]
            elif num - 1 in count:
                count[num] = count.get(num - 1) + 1
                count[num - count.get(num - 1)] = count[num]
            else:
                count[num] = 1
        return max(list(count.values()))
    
example = Solution()
print(example.longestConsecutive([100, 4, 200, 1, 3, 2]))