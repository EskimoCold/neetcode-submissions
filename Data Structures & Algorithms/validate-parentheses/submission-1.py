class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for el in s:
            if el in pairs.values():
                stack.append(el)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != pairs[el]:
                    return False

        return len(stack) == 0
