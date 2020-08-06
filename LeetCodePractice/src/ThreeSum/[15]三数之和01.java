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


import java.lang.reflect.Array;
import java.util.*;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution01 {
    public List<List<Integer>> threeSum(int[] nums) {
        // sort and three layer for loop
        // O(n^3)
        Arrays.sort(nums);

        Set<List<Integer>> ret = new LinkedHashSet<>();
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> line = Arrays.asList(nums[i], nums[j], nums[k]);
                        ret.add(line);
                    }
                }
            }
        }
        return new ArrayList<>(ret);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
