class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        seen = {}
        max_count = float('-inf')
        head = 0
        for tail in range(n):
            if s[tail] in seen and seen.get(s[tail]) >= head:
                head = seen.get(s[tail]) + 1
            seen[s[tail]] = tail
            count = tail - head + 1
            max_count = max(max_count, count)
        return max_count

example = Solution()
print(example.lengthOfLongestSubstring("abcabcbb"))