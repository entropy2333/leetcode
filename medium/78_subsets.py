class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrace(begin, path=[]):
            # print("candidates: {} path: {} res: {}".format(candidates, path))
            res.append(path[:])
            for index in range(begin, len(nums)):
                path.append(nums[index])
                backtrace(index + 1, path)
                path.pop()
        res = []
        path = []
        backtrace(0, path)
        return res