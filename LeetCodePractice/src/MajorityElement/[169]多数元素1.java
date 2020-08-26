package MajorityElement;
//给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
//
// 你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
//
// 
//
// 示例 1: 
//
// 输入: [3,2,3]
//输出: 3 
//
// 示例 2: 
//
// 输入: [2,2,1,1,1,2,2]
//输出: 2
// 
// Related Topics 位运算 数组 分治算法 
// 👍 718 👎 0


import java.util.Arrays;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution1 {
    public int majorityElement(int[] nums) {
        //  只要数组一定存在多数元素，个数就一定大于一半，那么1/长度 就是答案
        Arrays.sort(nums);
        int len = nums.length;

        return nums[len / 2];

    }
}
//leetcode submit region end(Prohibit modification and deletion)
