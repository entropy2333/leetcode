class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def fast_pow(base, exponent):
            bin_array = bin(exponent)[2:][::-1]
            n = len(bin_array)
            base_array = []

            pre_base = base
            base_array.append(pre_base)

            for i in range(n - 1):
                next_base = (pre_base * pre_base)
                base_array.append(next_base)
                pre_base = next_base

            res = multi(base_array, bin_array)
            return res

        def multi(base_array, bin_array):
            res = 1
            n = len(base_array)
            for i in range(n):
                base = base_array[i]
                if int(bin_array[i]) == 0:
                    continue
                res *= base
            return res
        return fast_pow(x, n) if n > 0 else fast_pow(1/x, -n)

if __name__ == '__main__':
    solution = Solution()
    result = solution.myPow(2, -10)
    print(result)