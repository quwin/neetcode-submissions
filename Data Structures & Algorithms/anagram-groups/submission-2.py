class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: dict[tuple[int, ...], list[str]] = {}
        def anagramKey(s: str) -> tuple[int, ...]:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            return tuple(counts)
        for s in strs:
            key = anagramKey(s)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())