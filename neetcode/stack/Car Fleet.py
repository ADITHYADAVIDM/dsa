class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
example = Solution()
print(example.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))