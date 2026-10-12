class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort + combine solution, greedy is awkward
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prior = res[-1]
            curr = intervals[i]
            if curr[0] <= prior[1]:
                res[-1] = [prior[0], max(prior[1], curr[1])]
            else:
                res.append(curr)

        return res