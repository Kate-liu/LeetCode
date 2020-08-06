# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2458 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        result = []

        if nums is None or nums_len < 3:
            return result

        nums.sort()

        for i in range(nums_len):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = nums_len - 1
            while L < R:
                summary = nums[i] + nums[L] + nums[R]
                if summary == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif summary > 0:
                    R -= 1
                elif summary < 0:
                    L += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = [1, -1, -1, 0]
    so = Solution()
    re = so.threeSum(s)
    print(re)
