class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size < 2:
            return nums
        path = []
        res = []
        nums.sort()
        self.backtrace(nums, size, path, res)
        return res

    def backtrace(self, candidates, size, path, res):
        print("candidates: {} size: {} path: {} res: {}".format(candidates, size, path, res))
        if not candidates:
            res.append(path[:])
            return
        for index in range(size):
            path.append(candidates[index])
            tmp = candidates[:]
            tmp.pop(index)
            self.backtrace(tmp, len(tmp), path, res)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    solution = Solution()
    result = solution.permute(candidates)
    print(result)