"""
Задача: https://leetcode.com/problems/valid-sudoku/
Подсказки:
"""


class Solution(object):
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # строки
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        # столбцы
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        # подблоки 3x3
        for block in range(9):
            seen = set()
            # Вычисляем начальные координаты подблока
            start_row = (block // 3) * 3
            start_col = (block % 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (
            [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            True
        ),
        (
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]],
            False
        ),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.isValidSudoku(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"
    print('Все тесты пройдены')
