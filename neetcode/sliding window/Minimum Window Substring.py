class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        rs = s
        tracker = {}
        left = -1
        bw = [0, 0]
        for ch in t:
            tracker[ch] = tracker.get(ch, 0) + 1
        matched = 0
        stable_window = False
        for right in range(len(s)):
            if stable_window:
                if s[right] in tracker:
                    tracker[s[right]] -= 1
                while s[left] not in tracker or tracker.get(s[left]) + 1 <= 0:
                    if s[left] in tracker:
                        tracker[s[left]] += 1
                    left += 1
                if right - left + 1 < bw[1]:
                    bw[0] = left
                    bw[1] = right - left + 1
            else:
                if left == -1 and s[right] in tracker:
                    left = right
                    tracker[s[right]] -= 1
                    matched += 1
                elif s[right] in tracker:
                    if tracker.get(s[right]) - 1 < 0:
                        tracker[s[right]] -= 1
                    else:
                        tracker[s[right]] -= 1
                        matched += 1
                if matched == len(t):
                    stable_window = True
                    bw[0] = left
                    bw[1] = right - left + 1
                    while s[left] not in tracker or tracker.get(s[left]) + 1 <= 0:
                        if s[left] in tracker:
                            tracker[s[left]] += 1
                        left += 1
                    if right - left + 1 < bw[1]:
                        bw[0] = left
                        bw[1] = right - left + 1
        return rs[bw[0]: bw[0] + bw[1]]

example = Solution()
print(example.minWindow("ADOBECODEBANC", "ABC"))