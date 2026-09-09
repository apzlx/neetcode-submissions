class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first use binary search to determine the row, then use binary search to determine the col
        # compare target to the first item of the middle row
        row_l = 0
        row_r = len(matrix)-1

        col_l = 0
        col_r = len(matrix[0])-1

        target_m = -1
        target_n = -1
        
        while row_l <= row_r:
            m = (row_r - row_l)//2+row_l
            if matrix[m][0] == target or matrix[m][-1] == target:
                return True
            if matrix[m][0] < target and matrix[m][-1] > target:
                target_m = m
                break
            if matrix[m][0] > target:
                row_r = m - 1
            else:
                row_l = m + 1
        print(target_m)
        while col_l <= col_r:
            n = (col_r - col_l)//2+col_l
            if matrix[target_m][n] == target:
                return True
            elif matrix[target_m][n] > target:
                col_r = n - 1
            else:
                col_l = n + 1
        
        return False
        
        
        

        