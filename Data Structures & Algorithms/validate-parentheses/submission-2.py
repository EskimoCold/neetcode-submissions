class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for el in s:
            if el in pairs:
                if not stack or stack.pop() != pairs[el]:
                    return False
            else:
                stack.append(el)   

        return len(stack) == 0
