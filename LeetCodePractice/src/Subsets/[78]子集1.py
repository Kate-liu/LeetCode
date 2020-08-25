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
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        self.dfs(0, nums, [], ret)
        return ret

    def dfs(self, level, nums, list, ret):
        # terminator
        if level == len(nums):
            ret.extend([list])
            return

        # process logic
        self.dfs(level + 1, nums, list, ret)
        list.append(nums[level])
        self.dfs(level + 1, nums, list, ret)

        # reverse current state


# leetcode submit region end(Prohibit modification and deletion)
