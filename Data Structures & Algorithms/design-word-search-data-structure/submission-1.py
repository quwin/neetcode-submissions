class WordDictionary:
    
    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            if curr.children[ord(word[i]) - ord('a')] is None:
                curr.children[ord(word[i]) - ord('a')] = WordDictionary()
            curr = curr.children[ord(word[i]) - ord('a')]
            if i == len(word) - 1:
                curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] == ".":
                if i == len(word) - 1:
                    return any(node is not None and node.end for node in curr.children)
                return any(node is not None and node.search(word[i+1:]) for node in curr.children)
            elif curr.children[ord(word[i]) - ord('a')] is None:
                return False
            else:
                curr = curr.children[ord(word[i]) - ord('a')]
            if i == len(word) - 1:
                return curr.end
        return True
        
