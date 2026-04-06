class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for ch in s:
            if ch in match.values():
                stack.append(ch)
            if ch in match:
                if not stack:
                    return False
                elif match[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack
                