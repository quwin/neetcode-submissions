class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Checked all pairs n times is O(n^2)
        # Looking for a better solution:
        # sort + simple linear iteration is O(nlogn)
        # Greedy can be O(n) but idk how
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output