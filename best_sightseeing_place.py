class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        minus = 0
        
        add = values[0]
        
        sol = 0
        for i range(1, len(values)):

            minus = max(minus, values[i]-i)


            sol = max(sol, minus+add)

            add = max(add, values[i]+i)

        return sol