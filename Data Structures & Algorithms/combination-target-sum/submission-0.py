class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(remaining, arr, path):
            if remaining == 0:
                res.append(path)
                return

            if remaining < 0:
                return

            for i in range(len(arr)):
                dfs(
                    remaining - arr[i],
                    arr[i:],
                    path + [arr[i]]
                )

        dfs(target, nums, [])
        return res