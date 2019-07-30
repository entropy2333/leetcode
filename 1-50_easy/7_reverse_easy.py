# 32ms 11.8MB
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         l = str(x).strip('0').split('-')
#         # x = 0
#         if l == ['']:
#             return 0
#         print(l)
#         # 负数保留负号
#         if l[0] == '' and (int(l[1][::-1]) < 2147483649):
#             return('-' + l[1][::-1])
#         elif l[0] != '' and (int(l[0][::-1]) < 2147483648):
#             return(l[0][::-1])
#         else:
#             return 0

# result = Solution().reverse(123)
# print(result)

# 36ms 11.7MB
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         s = str(x).strip('0')
#         if s.startswith('-'):
#             absnum = s[1:][::-1]
#             print(absnum)
#             if int(absnum) > 2147483648:
#                 return 0
#             return ('-' + absnum)
#         else:
#             absnum = s[::-1]
#             if absnum == '' or int(absnum) > 2147483647:
#                 return 0
#             return (absnum)

# result = Solution().reverse(0)
# print(result)        

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x < 0:
            absnum = int(s[1:][::-1])
            if absnum > 2147483648:
                return 0
            return (-absnum)
        else:
            absnum = int(s[::-1])
            if absnum > 2147483647:
                return 0
            return absnum

result = Solution().reverse(0)
print(result) 