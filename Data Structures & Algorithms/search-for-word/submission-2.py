class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking, quit as soon as an option is impossible
        # So use DFS with early quitting
        size = len(word)
        def backTrackSearch(idx: int, y: int, x: int, seen: set[tuple[int, int]]) -> bool:
            if idx == size:
                return True
            elif y < 0 or y == len(board) or x < 0 or x == len(board[y]):
                return False
            elif (y, x) in seen:
                return False
            seen.add((y,x))
            if board[y][x] == word[idx]:
                valid = (backTrackSearch(idx+1, y+1, x, seen)
                    or backTrackSearch(idx+1, y-1, x, seen)
                    or backTrackSearch(idx+1, y, x+1, seen)
                    or backTrackSearch(idx+1, y, x-1, seen)
                )
                seen.remove((y,x))
                return valid
            else:
                seen.remove((y,x))
            return False
        seen = set()
        for y in range(len(board)):
            for x in range(len(board[y])):
                if backTrackSearch(0, y, x, seen):
                    return True
        return False
