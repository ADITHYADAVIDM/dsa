class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        d = deque()
        l = [0] * len(temperatures)
        for i in range(len(temperatures)):
                while d and d[-1][0] < temperatures[i]:
                    l[d[-1][1]] = i - d[-1][1]
                    d.pop()
                d.append((temperatures[i], i))
        return l
example = Solution()
print(example.dailyTemperatures([73,74,75,71,69,72,76,73]))