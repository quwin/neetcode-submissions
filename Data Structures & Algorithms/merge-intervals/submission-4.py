class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Given a list of intervals (represented by a 2-len array),
        # How can I return that list such that all overlapping intervals
        # are merged. Overlapping means they have no common point,
        # Ending + Starting at the same time is overlapping
        # A basic solution is to have for each entry, check all over entries
        # To see if there's any overlaps, repeating if one is found.
        # That requires every item to check all other items, resulting in
        # O(n^2) time and O(1) space (if you are modifying the input array)
        # Another solution is to sort every entry and then move forwards 
        # across the sorted list. If an interval overlaps with the previous one,
        # merge them and continue, since it's in order you only need to check
        # one interval, the previous one.
        # This is O(n logn) time and O(n) space (depending on sorting algorithim)
        # An "optimal" solution takes into accout the fact that every merged int
        # Has only two key points:
        # The lowest possible start point, and the highest possible end point
        # From the highest end for every given start idx, you can merge them too
        # Exactly the same way but iterating over starts instead of every interval
        # This is O(m + n) time, O(m) space
        starting_idxs = {}
        maxStart = 0
        for interval in intervals:
            current_end = starting_idxs.setdefault(interval[0], interval[1])
            starting_idxs[interval[0]] = max(starting_idxs[interval[0]], interval[1])
            maxStart = max(maxStart, interval[0])

        res = []
        for start in range(maxStart+1):
            if start in starting_idxs:
                if len(res) == 0:
                    res.append([start, starting_idxs[start]])
                    continue
                else:
                    if res[-1][1] >= start:
                        res[-1][1] = max(res[-1][1], starting_idxs[start])
                    else:
                        res.append([start, starting_idxs[start]])
                        
        return res