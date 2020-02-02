class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        s = str.strip()
        d = ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = ''
        flag = 0
        start = True
        if not s:
            return 0
        if s[0] not in d:
            return 0
        for ch in s:
            if ch in d:
                start = False
                if ch == '-':
                    if flag == 0 and num == '':
                        flag = 1
                    else:
                        break
                elif ch == '+':
                    if flag == 0 and num == '':
                        flag = 2
                    else:
                        break
                else:
                    num += ch
            elif start:
                continue
            else:
                break
        if not num:
            return 0
        if flag == 0 or flag == 2:
            if int(num) > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(num)
        else:
            if int(num) > 2**31:
                return -2**31
            else:
                return -int(num)


print(Solution().myAtoi('0-1'))