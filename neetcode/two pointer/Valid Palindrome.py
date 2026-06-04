class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(ch.lower() for ch in s if ch.isalnum())
        i = 0
        j = len(c) - 1
        while i < j:
            if c[i] != c[j]:
                return False
            i += 1
            j -= 1
        return True

example = Solution()
print(example.isPalindrome("A man, a plan, a canal: Panapa"))