# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  示例: 
# 
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  说明: 
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。 
#  Related Topics 字符串 回溯算法 
#  👍 883 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(mapping[digits[0]])

        # 将前多个元素进行递归调用
        prev = self.letterCombinations(digits[:-1])

        add = mapping[digits[-1]]

        return [s + c for s in prev for c in add]

# leetcode submit region end(Prohibit modification and deletion)
