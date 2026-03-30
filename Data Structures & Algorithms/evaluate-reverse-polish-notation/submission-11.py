class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'

        stack = []

        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    c = int(a)+int(b)
                elif i == '-':
                    c = int(a)-int(b)
                elif i == '*':
                    c = int(a)*int(b)
                else:
                    c = int(int(a)/int(b))
                stack.append(str(c))
            print(stack)

        return int(stack[-1])