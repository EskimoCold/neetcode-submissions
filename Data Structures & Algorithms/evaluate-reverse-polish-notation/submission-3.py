class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()
            if token == '+':
                c = a + b
            elif token == '-':
                c = a - b
            elif token == '*':
                c = a * b
            else:
                c = int(a / b)

            stack.append(c)

        return stack[-1]
