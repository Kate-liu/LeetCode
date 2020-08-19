# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。 
# 
# 
#  返回滑动窗口中的最大值。 
# 
#  
# 
#  进阶： 
# 
#  你能在线性时间复杂度内解决此题吗？ 
# 
#  
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 508 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        Time complexity is O(n)
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        if n == 0:
            return []

        ans = []
        temp = max(nums[:k])

        for i in range(n - k):
            ans.append(temp)

            next_value = nums[i + k]
            if next_value > temp:
                temp = next_value
            else:
                if nums[i] == temp:
                    temp = max(nums[i + 1:i + 1 + k])
        ans.append(temp)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
