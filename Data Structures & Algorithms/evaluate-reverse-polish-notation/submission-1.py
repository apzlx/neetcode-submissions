class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set(["+", "-", "*", "/"])
        number_stack = []

        for t in tokens:
            if t in operator:
                num2 = number_stack.pop()
                num1 = number_stack.pop()
                res = 0
                match t:
                    case "+":
                        res = num1 + num2
                    case "-":
                        res = num1 - num2
                    case "*":
                        res = num1 * num2
                    case "/":
                        res = int(num1 / num2)

                number_stack.append(res)

            else:
                number_stack.append(int(t))
        
        return number_stack.pop()
