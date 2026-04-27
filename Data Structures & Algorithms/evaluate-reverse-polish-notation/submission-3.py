class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        
        stack = []
        for token in tokens:
            print(stack)
            if token in operators:
                a = stack.pop(-1)
                b = stack.pop(-1)
                if token == "+":
                    stack.append(b+a)
                if token == "-":
                    stack.append(b-a)
                if token == "*":
                    stack.append(b*a)
                if token == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[0]

        