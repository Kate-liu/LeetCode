package GenerateParentheses;//数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
//
// 
//
// 示例： 
//
// 输入：n = 3
//输出：[
//       "((()))",
//       "(()())",
//       "(())()",
//       "()(())",
//       "()()()"
//     ]
// 
// Related Topics 字符串 回溯算法 
// 👍 1254 👎 0


import java.util.ArrayList;
import java.util.List;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<String>();

        _generate("", 0, 0, n, list);

        return list;

    }

    private void _generate(String cur, int left, int right, int n, List<String> list) {
        // terminator
        if (left == n && right == n) {
            list.add(cur);
            return;
        }

        // process logic
        if (left < n) {
            _generate(cur + "(", left + 1, right, n, list);
        }
        if (right < left) {
            _generate(cur + ")", left, right + 1, n, list);
        }

    }
}
//leetcode submit region end(Prohibit modification and deletion)
