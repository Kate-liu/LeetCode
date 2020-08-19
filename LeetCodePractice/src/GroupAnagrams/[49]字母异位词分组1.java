package GroupAnagrams;//给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
//
// 示例: 
//
// 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
//输出:
//[
//  ["ate","eat","tea"],
//  ["nat","tan"],
//  ["bat"]
//] 
//
// 说明： 
//
// 
// 所有输入均为小写字母。 
// 不考虑答案输出的顺序。 
// 
// Related Topics 哈希表 字符串 
// 👍 435 👎 0


import java.util.*;
import java.util.stream.Stream;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution1 {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }

        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            // to array
            char[] ch = str.toCharArray();
            // then sort
            Arrays.sort(ch);
            // get map key
            String keyStr = String.valueOf(ch);
            // if not exist key, then put it
            if (!map.containsKey(keyStr)) {
                map.put(keyStr, new ArrayList<>());
            }
            // add origin string
            map.get(keyStr).add(str);
        }

        return new ArrayList<>(map.values());

    }
}
//leetcode submit region end(Prohibit modification and deletion)
