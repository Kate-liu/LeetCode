# 您需要在二叉树的每一行中找到最大的值。 
# 
#  示例： 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# 输出: [1, 3, 9]
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 87 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def largestValues(self, root):
        """
        used BFS method.
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        if not root:
            return result

        queue = collections.deque()
        queue.append(root)

        while queue:
            level_len = len(queue)

            maximum = float("-inf")

            for _ in range(level_len):
                node = queue.popleft()
                maximum = max(maximum, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(maximum)

        return result

# leetcode submit region end(Prohibit modification and deletion)
