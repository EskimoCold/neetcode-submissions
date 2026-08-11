class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = {}

        for i in range(9):
            row = set()
            column = set()

            for j in range(9):
                key = (i // 3, j // 3)

                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in column:
                        return False
                    column.add(board[j][i])

                if key not in sub_boxes:
                    sub_boxes[key] = set()

                if board[i][j] != '.':
                    if board[i][j] in sub_boxes[key]:
                        return False
                    
                    sub_boxes[key].add(board[i][j])                

        return True
