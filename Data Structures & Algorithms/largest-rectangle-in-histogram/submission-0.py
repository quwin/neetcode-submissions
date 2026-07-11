class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):

            currentHeight = 0 if i == len(heights) else heights[i]

            # While the current height is less than the last height:
            while stack and currentHeight < heights[stack[-1]]:
                priorIndex = stack.pop()
                height = heights[priorIndex]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height*width)

            stack.append(i)

        return maxArea