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

        def generate(p, left, right, parents=[]):
            if left:
                generate(p + '(', left - 1, right, parents)
            if right > left:
                generate(p + ')', left, right - 1, parents)

            if not right:
                parents.append(p)

            return parents

        return generate('', n, n)
# leetcode submit region end(Prohibit modification and deletion)
