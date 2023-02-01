# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
class Solution1:
    def helper(self, leftRoot: TreeNode, rightRoot: TreeNode) -> bool:
        if leftRoot is None and rightRoot is None:
            return True

        if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
            return False

        if leftRoot.val != rightRoot.val:
            return False

        return self.helper(leftRoot.left, rightRoot.right) and self.helper(leftRoot.right, rightRoot.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root.left, root.right)
        
''' Nested Function Recursive Solution
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root.left, root.right)
'''

# Iterative Solution
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if (left and right) and (left.val == right.val):
                stack.append((left.right, right.left))
                stack.append((left.left, right.right))
            elif not left and not right:
                continue
            else:
                return False
        return True

# Example
head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(2)
head.left.left = TreeNode(3)
head.right.right = TreeNode(3)
head.left.right = TreeNode(4)
head.right.left = TreeNode(4)

answer = Solution2()
print(answer.isSymmetric(head))
