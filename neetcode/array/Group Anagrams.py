class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            w = str(sorted(word))
            seen.setdefault(w, []).append(word)
        return [values for values in seen.values()]

example = Solution()
print(example.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))