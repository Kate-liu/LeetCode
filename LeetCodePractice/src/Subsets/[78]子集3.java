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
class Solution3 {
    public List<List<Integer>> subsets(int[] nums) {

        // for loop all already result add new element
        List<List<Integer>> result = new ArrayList<>();

        result.add(new ArrayList<>());

        for (int n : nums) {
            int size = result.size();

            for (int i = 0; i < size; i++) {
                List<Integer> subset = new ArrayList<>(result.get(i));

                subset.add(n);
                result.add(subset);
            }
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
