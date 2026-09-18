class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                index = 3 * (i//3) + j//3
                if num in rows[i]:
                    return False
                elif num in cols[j]:
                    return False
                elif num in boxes[index]:
                    return False
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[index].add(num)


        return True




        