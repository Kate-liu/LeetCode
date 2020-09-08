# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 494 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mySqrt(self, x):
        """
        method: 二分的思想，找中间数的平方不 与 目标数之间的关系
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        left, right = 1, x

        while left < right:
            # mid = left + (right - left) // 2
            # https://www.liwei.party/2019/06/17/leetcode-solution-new/search-insert-position/
            mid = (left + right + 1) >> 1

            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left

# leetcode submit region end(Prohibit modification and deletion)
