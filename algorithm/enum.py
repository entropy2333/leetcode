def enum(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    res = [[]]
    # print(dic)
    for num, freq in dic.items():
        temp = res.copy()
        for j in res:
            tmp = [j + [num] * (i + 1) for i in range(freq)]
            # print(j, num, tmp)
            temp.extend(j + [num] * (i + 1) for i in range(freq))
        res = temp
    return res

if __name__ == "__main__":
    nums = [1, 2, 2]
    res = enum(nums)
    print(res)