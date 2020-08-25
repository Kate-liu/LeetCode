package Subsets;//给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
//
// 说明：解集不能包含重复的子集。 
//
// 示例: 
//
// 输入: nums = [1,2,3]
//输出:
//[
//  [3],
//  [1],
//  [2],
//  [1,2,3],
//  [1,3],
//  [2,3],
//  [1,2],
//  []
//] 
// Related Topics 位运算 数组 回溯算法 
// 👍 720 👎 0


import java.util.ArrayList;
import java.util.List;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();

        if (nums == null) {
            return ret;
        }

        dfs(0, nums, new ArrayList<Integer>(), ret);
        return ret;
    }

    private void dfs(int level, int[] nums, ArrayList<Integer> list, List<List<Integer>> ret) {
        // terminator
        if (level == nums.length) {
            ret.add(new ArrayList<Integer>(list));
            return;
        }

        // process logic
        dfs(level + 1, nums, list, ret);  // no pick element

        list.add(nums[level]);
        dfs(level + 1, nums, list, ret); // pick element

        // reverse current state
        list.remove(list.size() - 1);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
