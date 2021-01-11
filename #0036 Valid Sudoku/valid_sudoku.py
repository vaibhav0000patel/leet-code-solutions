from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,columns,boxes = [{} for i in range(9)],[{} for i in range(9)],[{} for i in range(9)]
        
        for row_index in range(9):
            for col_index in range(9):
                
                num  = board[row_index][col_index]
                if num == '.':
                    continue

                box_offset = (row_index//3)*3+(col_index//3)
                
                rows[row_index][num] = rows[row_index].get(num,0)+1
                columns[col_index][num] = columns[col_index].get(num,0)+1
                boxes[box_offset][num] = boxes[box_offset].get(num,0)+1

                if  rows[row_index][num]>1  or \
                    columns[col_index][num]>1 or \
                    boxes[box_offset][num]>1:
                    return False
                    
        return True