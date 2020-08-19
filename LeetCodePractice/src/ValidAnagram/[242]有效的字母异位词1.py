# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表 
#  👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        Time complexity is O(N)
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}

        for item in s:
            dict1[item] = dict1.get(item, 0) + 1
        for item in t:
            dict2[item] = dict2.get(item, 0) + 1
        return dict1 == dict2

# leetcode submit region end(Prohibit modification and deletion)
