# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 637 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        time complexity is O(n)
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right

# leetcode submit region end(Prohibit modification and deletion)
