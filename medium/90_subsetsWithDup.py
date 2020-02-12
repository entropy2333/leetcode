class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrace(begin, path=[]):
            res.append(path[:])
            for index in range(begin, len(nums)):
                if index > begin and nums[index] == nums[index - 1]:
                    continue
                path.append(nums[index])
                backtrace(index + 1, path)
                path.pop()
        res = []
        path = []
        nums.sort()
        backtrace(0, path)
        return res

        '''
        # 先统计词频
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = [[]]
        for i, v in dic.items():
            temp = res.copy()
            for j in res:
                temp.extend(j+[i]*(k+1) for k in range(v))
            res = temp
        return res
        '''