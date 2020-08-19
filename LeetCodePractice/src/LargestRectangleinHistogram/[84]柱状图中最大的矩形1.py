# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 854 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        the time complexity is O(N)
        :type heights: List[int]
        :rtype: int
        """
        num = len(heights)
        left, right = [0] * num, [num] * num

        stack = list()

        for i in range(num):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ret = max((right[i] - left[i] - 1) * heights[i] for i in range(num)) if num > 0 else 0
        return ret

# leetcode submit region end(Prohibit modification and deletion)
