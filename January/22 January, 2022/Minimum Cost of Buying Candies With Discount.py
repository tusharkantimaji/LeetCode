class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        s = 0
        l = len(cost)
        # print(cost)
        for i in range(2, l, 3):
            s += cost[i]
        # print(s)
        return sum(cost)- s
        