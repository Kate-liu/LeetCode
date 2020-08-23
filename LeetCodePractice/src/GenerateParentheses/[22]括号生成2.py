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
            if left == 0 and right == 0:
                res.append(cur)
                return

            # process logic
            if right < left:
                return
            if left > 0:
                dfs(cur + "(", left - 1, right)
            if right > 0:
                dfs(cur + ")", left, right - 1)

        dfs(cur, n, n)
        return res

# leetcode submit region end(Prohibit modification and deletion)
