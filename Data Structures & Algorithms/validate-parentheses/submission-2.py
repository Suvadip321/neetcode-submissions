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
            elif ch in match:
                if not stack:
                    return False
                elif match[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return not stack
                