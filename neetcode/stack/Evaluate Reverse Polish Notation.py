class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}
        stack = []
        for ch in tokens:
            if ch in operations:
                match ch:
                    case '+':
                        top = stack.pop()
                        bottom = stack.pop()
                        stack.append(bottom + top)
                    case '-':
                        top = stack.pop()
                        bottom = stack.pop()
                        stack.append(bottom - top)
                    case '*':
                        top = stack.pop()
                        bottom = stack.pop()
                        stack.append(bottom * top)
                    case '/':
                        top = stack.pop()
                        bottom = stack.pop()
                        stack.append(math.floor(bottom / top) if (bottom > 0) == (top > 0) else math.ceil(bottom / top))
            else:
                stack.append(int(ch))
        return stack.pop()

example = Solution()
print(example.evalRPN(["2", "1", "+", "3", "*"]))