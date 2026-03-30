class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        decStack = []

        for i, t in enumerate(temperatures):
            
            while decStack and decStack[-1][0] < t:
                temp, indx = decStack.pop()
                res[indx] = i-indx
            
            decStack.append((t,i))
        
        return res