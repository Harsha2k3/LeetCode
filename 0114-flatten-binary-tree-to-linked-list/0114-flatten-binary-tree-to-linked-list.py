class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        # We follow right-left-root

        # Every time store the node in prev for which we
        # have computed the reverse postorder
        # and then for every node attach the prev to
        # right pointer while backtracking
        # (prev have the linked list that has reverse postoder till that point)
        # and attach None to left pointer of every node
        # while backtracking

        # https://www.youtube.com/watch?v=sWf7k1x9XR4&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=40
        # Watch from 3:00 to 10:00

        prev = None

        def rec(node):

            nonlocal prev

            if not node:
                return

            rec(node.right)
            rec(node.left)

            node.right = prev
            node.left = None
            prev = node

        rec(root)

        return root        