class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = []
        for i in range(rowIndex+1):
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
        return l[rowIndex]

# O(k)空间
class Solution(object):
    def getRow(self, rowIndex):
        # j行的数据, 应该由j - 1行的数据计算出来.
        # 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
        # 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r
