class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [(temperatures[0], 0)]
        res = [0 for i in range(len(temperatures))]

        for n in range(1, len(temperatures), 1):
            while tempStack and temperatures[n] > tempStack[-1][0]:
                res[tempStack[-1][1]] = n - tempStack[-1][1]
                tempStack.pop()
            tempStack.append((temperatures[n], n))

        return res

