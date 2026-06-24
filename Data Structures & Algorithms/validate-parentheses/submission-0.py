class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for key in s:
            if key == ']':
                if not stack:
                    return False
                if stack.pop() != "[":
                    return False
            elif key == ')':
                if not stack:
                    return False
                if stack.pop() != "(":
                    return False
            elif key == '}':
                if not stack:
                    return False
                if stack.pop() != "{":
                    return False
            else:
                stack.append(key)
        return not stack