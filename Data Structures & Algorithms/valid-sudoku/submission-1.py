class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = defaultdict(set)

        for i in range(9):
            row = set()
            column = set()

            for j in range(9):
                key = (i // 3, j // 3)
                val, transposed_val = board[i][j], board[j][i]

                if val != '.':
                    if val in row:
                        return False
                    row.add(val)

                if transposed_val != '.':
                    if transposed_val in column:
                        return False
                    column.add(transposed_val)

                if val != '.':
                    if val in sub_boxes[key]:
                        return False
                    
                    sub_boxes[key].add(val)

        return True
