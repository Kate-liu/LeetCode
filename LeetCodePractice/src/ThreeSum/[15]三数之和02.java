package ThreeSum;
//给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
//的三元组。 
//
// 注意：答案中不可以包含重复的三元组。 
//
// 
//
// 示例： 
//
// 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
//
//满足要求的三元组集合为：
//[
//  [-1, 0, 1],
//  [-1, -1, 2]
//]
// 
// Related Topics 数组 双指针 
// 👍 2458 👎 0


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution02 {
    public List<List<Integer>> threeSum(int[] nums) {
        // 排序后遍历，进行夹逼
        // O(n^2)
        List<List<Integer>> result = new ArrayList();

        int len = nums.length;

        if (nums == null || len < 3) {
            return result;
        }

        Arrays.sort(nums); // 首先对数组进行排序

        for (int i = 0; i < len; i++) {
            if (nums[i] > 0) {  // 如果 nums[i]大于 0，则三数之和必然无法等于 0，结束循环
                break;
            }
            if (i > 0 && nums[i] == nums[i - 1]) {  // 如果 nums[i] == nums[i-1]，则说明该数字重复，会导致结果重复，所以应该跳过
                continue;
            }

            int L = i + 1;
            int R = len - 1;
            while (L < R) {
                int sum = nums[i] + nums[L] + nums[R];
                if (sum == 0) {  // 满足条件
                    result.add(Arrays.asList(nums[i], nums[L], nums[R]));
                    while (L < R && nums[L] == nums[L + 1]) {
                        L++;
                    }
                    while (L < R && nums[R] == nums[R - 1]) {
                        R--;
                    }
                    L++;
                    R--;
                } else if (sum < 0) {  // 前提是排序好的数组，进行夹逼
                    L++;
                } else if (sum > 0) {  // 前提是排序好的数组，进行夹逼
                    R++;
                }
            }

        }
        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
