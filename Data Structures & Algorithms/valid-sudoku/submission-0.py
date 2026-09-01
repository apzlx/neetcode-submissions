class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # three constraints, rows, columns and the 3,3
        # brute force: go through all rows and columns and boxes to check for duplicates
        # each can be located in a set
        # a number can be part of the row, or column, or a 3X3 box, in total, there are 9*3 = 27 combos to check
        # board[i][j] where i = 0 j = 0-8 is a row
        # i = 0-8, j = 0 is a column
        # i,j = 0-2, i,j = 3-5, i,j=6-8
        # need a dict with keys for the constraint label, and values as set

        constraint = defaultdict(set)
        size = len(board)
        
        for row in range(size):
            for col in range(size):
                if board[row][col] != ".":
                    keys = (("r", row), ("c", col), (row//3, col//3))
                    if any(board[row][col] in constraint[key] for key in keys):
                        return False
                    for key in keys:
                        constraint[key].add(board[row][col]) 
        return True


