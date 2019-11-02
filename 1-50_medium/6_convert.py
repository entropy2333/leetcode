class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1 or numRows == 1 or len(s) <= numRows:
            return s
        mod = 2*numRows - 2
        num = len(s) % mod - 1
        k = len(s) // mod
        # len(s) = k*mod + num
        s_convert = ''
        if num < numRows:
            """
            0            k*mod
            1       k*mod-1
                         ...
            num          k*mod+num
            ...  
            Row-1
            """
            for j in range(numRows):
                for i in range(k+1):
                    if j == 0:
                        if num == -1:
                            if i < k:
                                s_convert += s[i*mod]
                        else:
                            s_convert += s[i*mod]
                    elif j == (numRows-1):
                        if num == (numRows-1):
                            s_convert += s[i*mod+(numRows-1)]
                        else:
                            if i < k:
                                s_convert += s[i*mod+(numRows-1)]
                        continue
                    elif j <= num and j < (numRows-1):
                        if i == 0:
                            s_convert += s[j]
                            continue
                        s_convert += s[i*mod-j]
                        s_convert += s[i*mod+j]
                    elif j > num and j < (numRows-1) and i < k:
                        s_convert += s[i*mod+j]
                        s_convert += s[(i+1)*mod-j]
        else:
            """
            0            k*mod
            1       k*mod-1
                         
            num          ...     k*mod+num
            ...  
            Row-1
            """
            for j in range(numRows):
                for i in range(k+1):
                    if j == 0:
                        s_convert += s[i*mod]
                    elif j == (numRows-1):
                        s_convert += s[i*mod+(numRows-1)]
                    elif j < (mod-num) and j < (numRows-1):
                        if i == 0:
                            s_convert += s[j]
                            continue
                        s_convert += s[i*mod-j]
                        s_convert += s[i*mod+j]
                    elif j >= (mod-num) and j < (numRows-1):
                        s_convert += s[i*mod+j]
                        s_convert += s[(i+1)*mod-j]
        print(s_convert)
        return s_convert

s="PAYPALISHIRING"
print(len(s))
Solution().convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
, 4)