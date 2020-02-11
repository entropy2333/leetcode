class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size < 1:
            return nums
        path = []
        res = []
        nums.sort()
        self.backtrace(nums, path, res)
        return res

    def backtrace(self, candidates, path, res):
        print("candidates: {} path: {} res: {}".format(candidates, path, res))
        if not candidates:
            res.append(path[:])
            return
        for index in range(len(candidates)):
            if index != 0 and candidates[index] == candidates[index-1]:
                continue
            path.append(candidates[index])
            self.backtrace(candidates[:index]+candidates[index+1:], path, res)
            path.pop()

if __name__ == '__main__':
    candidates = [1, 2, 6]
    solution = Solution()
    result = solution.permuteUnique(candidates)
    print(result)