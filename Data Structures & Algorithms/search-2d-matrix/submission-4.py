class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            middle_idx = (l + r) // 2
            middle_value = matrix[middle_idx // m][middle_idx % m]

            if middle_value == target:
                return True
            elif middle_value < target:
                l = middle_idx + 1
            else:
                r = middle_idx - 1

        return False

            