def backtrace(candidates, path=[], res=[]):
    print("candidates: {} path: {} res: {}".format(candidates, path, res))
    if not candidates:
        res.append(path[:])
        return
    for index in range(len(candidates)):
        path.append(candidates[index])
        backtrace(candidates[:index]+candidates[index+1:], path, res)
        path.pop()

if __name__ == '__main__':
    candidates = [1, 2, 3]
    result = backtrace(candidates)
    print(result)