class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 0 or n == 1:
            return intervals
        intervals.sort()
        res = []
        left = 0
        right = 0
        for i,interval in enumerate(intervals):
            if i == 0:
                left = interval[0]
                right = interval[1]
            else:
                cur_left = interval[0]
                cur_right = interval[1]
                if cur_left <= right:
                    right = max(cur_right, right)
                    continue
                else:
                    res.append([left, right])
                    left, right = cur_left, cur_right
        res.append([left, right])
        return res

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[11,18]]
    res = s.merge(intervals)
    print(res)