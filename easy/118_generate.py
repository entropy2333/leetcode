class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for i in range(numRows):
            if i == 0:
                l.append([1])
            else:
                tmp = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        tmp.insert(j, 1)
                    else:
                        tmp.insert(j, l[i-1][j] + l[i-1][j-1])
                l.append(tmp)
        return l
