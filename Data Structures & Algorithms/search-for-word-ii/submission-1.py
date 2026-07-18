class Solution:
    
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.index = -1

        def add(self, word: str, index: int):
            curr = self
            for char in word:
                if curr.children[ord(char) - ord('a')] is None:
                    curr.children[ord(char) - ord('a')] = Solution.TrieNode()
                curr = curr.children[ord(char) - ord('a')]
            curr.index = index
        
        def search(self, word: str) -> int:
            curr = self
            for char in word:
                if curr.children[ord(char) - ord('a')] is None:
                    return False
                curr = curr.children[ord(char) - ord('a')]
            return curr.index
        
        def traverse(self, char: str) -> Optional[TrieNode]:
            return self.children[ord(char[0]) - ord('a')]
                

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Two ideas: 
        ## Turn words into Trie
        ## Turn board into Trie
        ## Need to define word endings so must use words into Trie
        trie = self.TrieNode()
        for i, word in enumerate(words):
            trie.add(word, i)
        results = []
        directions = ["LEFT", "RIGHT", "UP", "DOWN"]

        def dfs(y: int, x: int, traveled: set[tuple[int, int]], curr: Optional[Solution.TrieNode]):
            if curr is None:
                return
            # Makes a new copy every bfs, how else do I do this?
            newSet = traveled.copy()
            newSet.add((y, x))
            if curr.index != -1:
                results.append(words[curr.index])
                curr.index = -1
            for direction in directions:
                newY, newX = y, x
                match direction:
                    case "LEFT":
                        newX = x - 1
                    case "RIGHT":
                        newX = x + 1
                    case "UP":
                        newY = y + 1
                    case "DOWN":
                        newY = y - 1
                if (newY, newX) not in traveled and newY >= 0 and newX >= 0 and newY < len(board) and newX < len(board[y]):
                    dfs(newY, newX, newSet, curr.traverse(board[newY][newX]))

        # Graph DFS per tile (144x)
        for y in range(len(board)):
            for x in range(len(board[y])):
                node = trie.traverse(board[y][x])
                dfs(y, x, set(), node)

        return results


