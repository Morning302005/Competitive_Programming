class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False

        return len(stack) == 0