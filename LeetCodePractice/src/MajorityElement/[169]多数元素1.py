# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        Time complexity is O(n)
        :type nums: List[int]
        :rtype: int
        """

        dic = {}

        # 字典存储重复元素的个数
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        # 看一下那个元素的长度大于 1/2 长度
        for num in nums:
            if dic[num] > len(nums) // 2:
                return num
# leetcode submit region end(Prohibit modification and deletion)
