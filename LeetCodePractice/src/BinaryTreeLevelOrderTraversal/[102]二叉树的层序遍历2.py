# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 615 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        use DFS method
        time complexity is O(N)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if not root:
            return result

        self.travel(root, 1, result)
        return result

    def travel(self, node, level, result):
        # terminator
        if not node:
            return

        if level > len(result):
            result.append([node.val])
        else:
            result[level - 1].extend([node.val])

        if node.left:
            self.travel(node.left, level + 1, result)
        if node.right:
            self.travel(node.right, level + 1, result)
# leetcode submit region end(Prohibit modification and deletion)
