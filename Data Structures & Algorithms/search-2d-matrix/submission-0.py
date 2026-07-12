class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        yStart, yEnd = 0, len(matrix) - 1
        while yStart <= yEnd :
            mid = yEnd-yStart // 2
            start, end = matrix[mid][0], matrix[mid][-1]
            if start <= target and end >= target:
                xStart, xEnd = 0, len(matrix[mid]) - 1
                while xStart <= xEnd:
                    xMid = xEnd-xStart // 2
                    num = matrix[mid][xMid]
                    if num == target:
                        return True
                    elif num < target:
                        xStart = xMid + 1
                    else:
                        xEnd = xMid - 1
                return False
            elif start < target and end < target:
                yStart = mid+1
            elif start > target and end > target:
                yEnd = mid-1            
        return False