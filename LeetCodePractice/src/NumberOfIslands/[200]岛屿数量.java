package NumberOfIslands;//给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
//
// 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
//
// 此外，你可以假设该网格的四条边均被水包围。 
//
// 
//
// 示例 1: 
//
// 输入:
//[
//['1','1','1','1','0'],
//['1','1','0','1','0'],
//['1','1','0','0','0'],
//['0','0','0','0','0']
//]
//输出: 1
// 
//
// 示例 2: 
//
// 输入:
//[
//['1','1','0','0','0'],
//['1','1','0','0','0'],
//['0','0','1','0','0'],
//['0','0','0','1','1']
//]
//输出: 3
//解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
// 
// Related Topics 深度优先搜索 广度优先搜索 并查集 
// 👍 735 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {

    public int numIslands(char[][] grid) {
        // used DFS method

        if (grid.length == 0) {
            return 0;
        }

        int count = 0;
        int xSize = grid.length;
        int ySize = grid[0].length;

        for (int x = 0; x < xSize; x++) {
            for (int y = 0; y < ySize; y++) {
                char cur = grid[x][y];
                if (cur == '1') {
                    count += 1;
                    helper(x, y, grid);
                }
            }
        }

        return count;
    }

    private void helper(int x, int y, char[][] grid) {
        grid[x][y] = '0';

        if (x - 1 >= 0 && grid[x - 1][y] == '1') {
            helper(x - 1, y, grid);
        }
        if (x + 1 < grid.length && grid[x + 1][y] == '1') {
            helper(x + 1, y, grid);
        }
        if (y - 1 >= 0 && grid[x][y - 1] == '1') {
            helper(x, y - 1, grid);
        }
        if (y + 1 < grid[0].length && grid[x][y + 1] == '1') {
            helper(x, y + 1, grid);
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)
