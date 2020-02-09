class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            res = []
            res.append(1)
            for i in range(1, n+1):
                res.append(res[i-1]*i)
            return res[n]
        
        def getPath(candidates, n, k, path):
            if n == 1:
                return path + candidates[0]
            fact = factorial(n - 1)
            index, k = divmod(k, fact)
            path += candidates[index]
            return getPath(candidates[:index] + candidates[index+1:], n - 1, k, path)
        
        candidates = [str(i) for i in range(1, n + 1)]
        return getPath(candidates, n, k - 1, '')