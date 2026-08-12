class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            current_t = temperatures[i]
            t = 0
            while stack and t <= current_t:
                t, idx = stack.pop()
            if t > current_t:
                stack.append((t, idx))
                result[i] = idx - i

            stack.append((current_t, i))

        return result
