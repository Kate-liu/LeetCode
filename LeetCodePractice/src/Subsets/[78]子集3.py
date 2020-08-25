# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 720 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def subsets(self, nums):
        """
        use library function
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):  # combinations object
                result.append(tmp)

        return result

# leetcode submit region end(Prohibit modification and deletion)
