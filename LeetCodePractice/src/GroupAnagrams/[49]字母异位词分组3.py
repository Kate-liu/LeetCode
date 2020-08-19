# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 435 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Time complexity is O(N^2)
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = collections.defaultdict(list)

        for str in strs:
            array = [0] * 26
            for s in str:
                array[ord(s) - ord('a')] += 1

            key = tuple(array)
            hmap[key].append(str)

        return list(hmap.values())

# leetcode submit region end(Prohibit modification and deletion)
