class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxzy',
        }
        l = list(digits)
        res = ['']
        for i in range(len(l)):
            l[i] = d[l[i]]
            tmp = []
            for ch in l[i]:
                for s in res:
                    tmp.append(s + ch)
            res = tmp
            
        return res