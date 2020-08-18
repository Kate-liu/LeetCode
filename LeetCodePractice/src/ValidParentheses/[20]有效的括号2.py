# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串 
#  👍 1801 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        Time Complexity: O(N)
        :type s: str
        :rtype: bool
        """
        stack = []
        dictionary = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                if stack == [] or dictionary[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
# leetcode submit region end(Prohibit modification and deletion)
