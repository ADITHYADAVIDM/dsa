class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        seen = {}
        max_count = float('-inf')
        count = 0
        head = 0
        for tail in range(n):
            if s[tail] in seen:
                if(seen.get(s[tail])) + 1 < n:
                    head = (seen.get(s[tail])) + 1
                    seen = {alpha: index for alpha, index in seen.items() if index >= head}
                    seen[s[tail]] = tail
                    max_count = max(max_count, count)
                else:
                    return max_count
            else:
                seen[s[tail]] = tail
                count = tail - head + 1
        max_count = max(max_count, count)
        return max_count

example = Solution()
print(example.lengthOfLongestSubstring("abcabcbb"))