class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        r = []
        for s in path.split('/'):
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
            print(r)
        return '/' + '/'.join(r)

if __name__ == "__main__":
    s = Solution()
    path = "/a//b////c/d//././/.."
    res = s.simplifyPath(path)
    print('res: {}'.format(res))