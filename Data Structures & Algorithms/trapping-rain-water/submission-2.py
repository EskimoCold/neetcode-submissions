class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [height[0]]
        max_rights = [height[-1]]
        result = 0

        for i in range(1, len(height)):
            current_left = height[i]
            current_right = height[-(i + 1)]
            max_lefts.append(max(max_lefts[-1], current_left))
            max_rights.append(max(max_rights[-1], current_right))

        for i in range(1, len(height) - 1):
            current = height[i]
            max_left = max_lefts[i - 1]
            max_right = max_rights[-(i + 1)]
            result += max(0, min(max_left, max_right) - current)
        
        return result