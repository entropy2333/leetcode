# func1可以判断空列表、空字符串、True/False以及None
def func1(x):
    return not x

def func2(x):
    return x is None

# func3与func2结果相反
def func3(x):
    return x is not None

# func4与func1结果相反
def func4(x):
    return True if x else False

if __name__ == "__main__":
    a = []
    b = True
    c = False
    d = None
    e = ''
    l = [a, b, c, d, e]
    res1 = list(map(func1, l))
    res2 = list(map(func2, l))
    res3 = list(map(func3, l))
    res4 = list(map(func4, l))
    print(res1, res2, res3, res4, sep='\n')