# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 829 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self._dfs(0, nums, [])
        return self.ret

    def _dfs(self, level: int, nums, cur):
        if len(nums) == 0:
            self.ret.append(cur)
            print(cur)
            return
        for i in range(len(nums)):
            if nums[i] not in cur:
                new_cur = cur + [nums[i]]
                new_nums = nums[0:i] + nums[i + 1:]  # reduce self used element
                self._dfs(level + 1, new_nums, new_cur)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = [1, 2, 3, 4]
    so = Solution()
    so.permute(s)
