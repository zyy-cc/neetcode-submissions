class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        match = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for ele in s:
            if ele in match:
                # if it's empty or the last one is not matched
                if not stack or stack[-1] != match[ele]:
                    return False
                stack.pop()
            else:
                stack.append(ele)
        
        return not stack




           