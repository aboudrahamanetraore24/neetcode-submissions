class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in s:
                    return False
                else:
                    s.add(v)

            for j in range(9):
                s = set()
                for i in range(9):
                    v = board[i][j]
                    if v == ".":
                        continue
                    if v in s:
                        return False
                    else:
                        s.add(v)
            for i in range(0,9,3):
                for j in range(0,9,3):
                    s = set()
                    for k in range(3):
                        for l in range(3):
                            v = board[i+k][(j+l)]
                            if v == ".":
                                continue
                            if v in s:
                                return False
                            else:
                                s.add(v)
        return True   
        