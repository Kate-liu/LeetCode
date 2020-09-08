# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划 
#  👍 800 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        BFS method
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        value1 = [0]
        value2 = []
        nc = 0
        visited = [False] * (amount + 1)
        visited[0] = True

        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newVal = v + coin

                    if newVal == amount:
                        return nc
                    elif newVal > amount:
                        continue
                    elif not visited[newVal]:
                        visited[newVal] = True
                        value2.append(newVal)
            value1, value2 = value2, []

        return -1
# leetcode submit region end(Prohibit modification and deletion)
