class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        self.__dfs(candidates, 0, path, res, target)
        return res

    def __dfs(self, candidates, begin, path, res, target):
        # print("candidates: {} path: {} res: {} target: {}".format(candidates, path, res, target))
        # 先写递归终止的情况
        if target == 0:
            res.append(path[:])
            return
        
        for index in range(begin, len(candidates)):
            if (index > begin and candidates[index] == candidates[index-1]):
                continue
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.__dfs(candidates[:index]+candidates[index+1:], index, path, res, residue)
            path.pop()