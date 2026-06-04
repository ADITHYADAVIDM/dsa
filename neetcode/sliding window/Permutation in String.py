class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tracker = {}
        for ch in s1:
            tracker[ch] = tracker.get(ch, 0) + 1
        left = 0
        for right in range(len(s2)):
            ch = s2[right]
            tracker[ch] = tracker.get(ch, 0) - 1
            while tracker[ch] < 0:
                tracker[s2[left]] += 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False

example = Solution()
print(example.checkInclusion("ab", "abdul"))