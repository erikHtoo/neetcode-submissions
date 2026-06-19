class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # stack = [(temp, index)]
        tempStack = [(temperatures[0], 0)]
        print("tempStack: ", tempStack)
        res = [0 for i in range(len(temperatures))]
        print("res: ", res)

        for n in range(1, len(temperatures), 1):
            print("n: ", n)
            print("temperatures[n]: ", temperatures[n])
            print("tempStack[-1]: ", tempStack[-1])
            while tempStack and temperatures[n] > tempStack[-1][0]:
                res[tempStack[-1][1]] = n - tempStack[-1][1]
                print(res)
                tempStack.pop()
            tempStack.append((temperatures[n], n))
            print("tempStack: ", tempStack)
            print("#############")

        return res

