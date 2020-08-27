# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  示例: 
# 
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
# ，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 516 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []

        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

        self.DFS(0, n, [])
        return self._generate_result(n)

    def DFS(self, row, n, cur_state):
        # terminator
        if row >= n:
            self.result.append(cur_state)
            return

        # process logic
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue

            # drill down
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            # recursion
            self.DFS(row + 1, n, cur_state + [col])

            # reverse state
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))

        return [board[i:i + n] for i in range(0, len(board), n)]
# leetcode submit region end(Prohibit modification and deletion)
