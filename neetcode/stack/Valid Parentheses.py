class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        l = []
        for ch in s:
            if ch in d:
                l.append(ch)
            elif l:
                if ch == d[l[-1]]:
                    l.pop()
                else:
                    return False
            else:
                return False
        if l:
            return False
        else:
            return True

example = Solution()
print(example.isValid("()"))