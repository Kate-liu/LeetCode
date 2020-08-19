package LargestRectangleinHistogram;//给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
//
// 求在该柱状图中，能够勾勒出来的矩形的最大面积。 
//
// 
//
// 
//
// 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
//
// 
//
// 
//
// 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
//
// 
//
// 示例: 
//
// 输入: [2,1,5,6,2,3]
//输出: 10 
// Related Topics 栈 数组 
// 👍 854 👎 0


import java.util.Stack;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int largestRectangleArea(int[] heights) {
        // the time complexity is O(N)
        int len = heights.length;

        Stack<Integer> stack = new Stack<>();

        int area = 0;

        for (int i = 0; i <= len; i++) {
            int h = (i == len ? 0 : heights[i]);

            if (stack.isEmpty() || h >= heights[stack.peek()]) {
                stack.push(i);
            } else {
                int tp = stack.pop();
                area = Math.max(area, heights[tp] * (stack.isEmpty() ? i : i - stack.peek() - 1));
                i--;
            }
        }
        return area;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
