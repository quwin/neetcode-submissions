class PrefixTree:

    def __init__(self, char = ''):
        self.children: dict[str, PrefixTree] = {}
        self.char = char
        self.word_ending: bool = False

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            ending = i == len(word) - 1
            curr = curr.children.setdefault(word[i], PrefixTree(word[i]))
            if ending:
                curr.word_ending = True


    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            ending = i == len(word) - 1
            curr = curr.children[word[i]]
            if ending:
                return curr.word_ending

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        return True
        