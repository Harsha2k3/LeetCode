class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        res = []

        pm = {}      # Parent Map

        seen = set()

        def getParent(root , parent):

            if root is None:
                return 

            pm[root] = parent 

            getParent(root.left , root)
            getParent(root.right , root)


        def dfs(target , k):

            nonlocal res

            if not target or target in seen:
                return 

            seen.add(target)
            
            if k == 0:
                res.append(target.val)

            dfs(target.left , k - 1)
            # k += 1
            dfs(target.right , k - 1)
            dfs(pm[target] , k - 1)

            return res

        getParent(root , None)

        return dfs(target , k)