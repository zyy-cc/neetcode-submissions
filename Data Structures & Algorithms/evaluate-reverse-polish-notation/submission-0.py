class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    res = a + b
                    stack.append(res)
                elif t == "-":
                    res = a - b
                    stack.append(res)
                elif t == "*":
                    res = a * b
                    stack.append(res)
                elif t == "/":
                    res = int(a/b)
                    stack.append(res)
        return stack[-1]

        