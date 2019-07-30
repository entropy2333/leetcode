# 24ms 11.5MB
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        judge = {'()', '[]', '{}'}
        for i, ch in enumerate(s):
            if not stack:
                stack.append(ch)
            elif stack[-1] + ch in judge:
                stack.pop()
            else:
                stack.append(ch)
        return stack == []
        
print(Solution().isValid("[](]"))