from typing import List

def sudoku(puzzle: List[List[int]]) -> List[List[int]]:
    assert len(puzzle) == 9 and all(len(row) == 9 for row in puzzle), "Invalid puzzle size"

    def is_valid(row: int, col: int, num: int) -> bool:
        if num in puzzle[row]:
            return False

        if num in [puzzle[i][col] for i in range(9)]:
            return False

        start_row, start_col = row - row % 3, col - col % 3
        
        for i in range(3):
            for j in range(3):
                if puzzle[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve() -> bool:
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            puzzle[row][col] = num
                            
                            if solve():
                                return True
                            
                            puzzle[row][col] = 0
                            
                    return False
                
        return True

    # Once again, I hate this nesting of for loops,
    # But 'solve' uses a backtracking algorithm, so
    # It's efficient.

    solve()
    
    return puzzle
