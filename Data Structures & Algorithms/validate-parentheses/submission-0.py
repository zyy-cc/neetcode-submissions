class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for ele in s:
            if stack:
                if stack[-1] == "(" and ele == ")":
                    stack.pop()
                elif stack[-1] == "{" and ele == "}":
                    stack.pop()
                elif stack[-1] == "[" and ele == "]":
                    stack.pop()
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
        
        if stack:
            return False
        else:
            return True




           