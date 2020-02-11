class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        def backtrace(begin, path=[]):
            # print("candidates: {} path: {} res: {}".format(candidates, path))
            if len(path) == k:
                res.append(path[:])
                return
            for index in range(begin, n):
                path.append(index + 1)
                backtrace(index + 1, path)
                path.pop()
        res = []
        path = []
        backtrace(0, path)
        return res

class Solution:
    def combine(self, n, k):
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
            
        return output

if __name__ == "__main__":
    s = Solution()
    res = s.combine(4, 2)
    print('res: {}'.format(res))