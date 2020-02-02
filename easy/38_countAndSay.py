class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        m = self.countAndSay(n - 1)
        d = {}
        count = 1
        i = j = 0
        while i < len(m):
            j = i + 1
            while j < len(m) and m[j] == m[i]:
                count += 1
                j += 1
            s += str(count) + str(m[i])
            i += count
            count = 1
        return s
for i in range(1, 10):    
    print(Solution().countAndSay(i))