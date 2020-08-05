package ValidPalindrome;//给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
//
// 说明：本题中，我们将空字符串定义为有效的回文串。 
//
// 示例 1: 
//
// 输入: "A man, a plan, a canal: Panama"
//输出: true
// 
//
// 示例 2: 
//
// 输入: "race a car"
//输出: false
// 
// Related Topics 双指针 字符串 
// 👍 259 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean isPalindrome(String s) {
        // 1.filter non-number and non-char
        String filtered = _filterNonNumberAndChar(s);
        // 2.reverse filtered string
        String reversed = _reverseFiltered(filtered);
        // 3.equals
        return filtered.equalsIgnoreCase(reversed);
    }

    private String _reverseFiltered(String filtered) {
        return new StringBuilder(filtered).reverse().toString();
    }

    private String _filterNonNumberAndChar(String s) {
        return s.replaceAll("[^A-Za-z0-9]", "");
    }
}
//leetcode submit region end(Prohibit modification and deletion)
