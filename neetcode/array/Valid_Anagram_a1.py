class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        look_up = {}
        for ch in s:
            look_up[ch] = look_up.get(ch, 0) + 1
        for ch in t:
            if ch in look_up:
                look_up[ch] -= 1
            else:
                return False
        for value in look_up.values():
            if value != 0:
                return False
        return True
    
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))