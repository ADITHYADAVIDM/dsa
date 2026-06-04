class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        max_len = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            w = right - left + 1
            if w - max_freq > k:
                count[s[left]] -= 1
                left += 1
            w = right - left + 1
            max_len = max(max_len, w)
        return max_len

example = Solution()
print(example.characterReplacement("ABAB", 2))