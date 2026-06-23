class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: list[set[int]] = [set() for _ in range(9)]
        columns: list[set[int]] = [set() for _ in range(9)]
        cubes: list[set[int]] = [set() for _ in range(9)]
        gridIndex = -3
        for y, row in enumerate(board):
            for x, slot in enumerate(row):
                if y%3 == 0 and x==0:
                    gridIndex = gridIndex+3
                if slot == '.':
                    continue
                cubeIndex = gridIndex + int(x/3)
                num = int(slot)
                if num in rows[y]:
                    return False
                if num in columns[x]:
                    return False
                if num in cubes[cubeIndex]:
                    return False
                rows[y].add(num)
                columns[x].add(num)
                cubes[cubeIndex].add(num)
        return True