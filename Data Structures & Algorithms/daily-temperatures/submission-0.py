class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            T = temperatures[i]
            if not stack:
                stack.append(i)
            else:
                while stack and T > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = i - idx
                stack.append(i)

        return res


        