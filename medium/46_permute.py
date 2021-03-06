class Solution(object):
    def permute(self, nums):
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
            path.append(candidates[index])
            self.backtrace(candidates[:index]+candidates[index+1:], path, res)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    solution = Solution()
    result = solution.permute(candidates)
    print(result)