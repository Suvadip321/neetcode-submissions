class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if ch in match:
                if not stack:
                    return False
                elif stack[-1] != match[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return not stack