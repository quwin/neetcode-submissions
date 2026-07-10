class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        monoStack = [] # in pairs to keep the index (num, index)
        i = 0
        for i, temp in enumerate(temperatures):
            while monoStack and temp > monoStack[-1][0]:
                stackIdx = monoStack.pop()[1]
                output[stackIdx] = i - stackIdx

            monoStack.append((temp, i))
        return output
            
            