class Solution:
    def operate(self, num1: int, num2: int, operand: str) -> int:
        if operand == '+':
            return num1+num2
        elif operand == '-':
            return num1-num2
        elif operand == '*':
            return num1*num2
        else:
            return int(num1/num2)


    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        midStack = []
        for token in tokens:
            if token in operands:
                num2 = midStack.pop()
                num1 = midStack.pop()
                midStack.append(self.operate(num1, num2, token))
            else:
                midStack.append(int(token))
            
        return midStack.pop()