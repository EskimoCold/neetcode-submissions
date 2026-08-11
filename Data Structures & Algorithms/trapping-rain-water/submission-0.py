class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [height[0]]
        max_rights = [height[-1]]
        current = height[0]
        result = 0

        for i in range(1, len(height)):
            current = height[i]
            max_lefts.append(max(max_lefts[-1], current))

        current = height[-1]

        for i in range(len(height) - 2, -1, -1):
            current = height[i]
            max_rights.append(max(max_rights[-1], current))

        max_rights = max_rights[::-1]

        for i in range(1, len(height) - 1):
            current = height[i]
            max_left = max_lefts[i - 1]
            max_right = max_rights[i + 1]
            result += max(0, min(max_left, max_right) - current)
        
        return result