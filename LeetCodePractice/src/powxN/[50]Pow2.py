# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。 
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
#  Related Topics 数学 二分查找 
#  👍 476 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        time complexity is O(log n)
        分治算法，递归运算
        :type x: float
        :type n: int
        :rtype: float
        """

        def quickPow(N):
            if N == 0:
                return 1.0

            y = quickPow(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickPow(n) if n >= 0 else 1.0 / quickPow(-n)

# leetcode submit region end(Prohibit modification and deletion)
