class Solution:

    def encode(self, strs: List[str]) -> str:
        string = str()
        for word in strs:
            string = string + str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        ans = []
        pointer = 0;
        while pointer < len(s):
            delimiter = s.find("#", pointer)
            length = int(s[pointer:delimiter])
            ans.append(s[delimiter+1:delimiter+1+length])
            pointer = delimiter + 1 + length
        return ans