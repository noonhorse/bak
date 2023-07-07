​​#!/usr/bin/env python​​
print("hello world")

# 二叉树宽度遍历
# 递归
class Solution:
        def widthOfBinaryTree(self, root):
            if not root:
                return 0
            left = self.widthOfBinaryTree(root.left)
            right = self.widthOfBinaryTree(root.right)
            return max(left, right) + 1
            # return max(self.widthOfBinaryTree(root.left), self.widthOfBinaryTree(root.right)) + 1
            
