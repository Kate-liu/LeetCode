# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        cur = ''

        if n == 0:
            return res

        def dfs(cur, left, right):
            # terminator
            if left == n and right == n:
                res.append(cur)
                return

            # process logic
            if left < n:
                dfs(cur + "(", left + 1, right)
            if right < left:  # get right < n
                dfs(cur + ")", left, right + 1)

        dfs(cur, 0, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
