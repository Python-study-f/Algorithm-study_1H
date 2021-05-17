N = input()

def dfs(num, n, ok):        # ok True : 최댓값, False : 최솟값
    if len(num) == 1:       
        if int(num[0]) % 2 != 0:
            n += 1
        return n
    elif len(num) == 2:
        if int(num[0]) % 2 != 0:
            n += 1
        if int(num[1]) % 2 != 0:
            n += 1
        return dfs(str(int(num[0]) + int(num[1])), n, ok)
    else:
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                n += 1
        result = 0
        if ok:
            result = 0
        else:
            result = 100000000
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                a = int(num[:i])
                b = int(num[i:j])
                c = int(num[j:])
                if ok:
                    result = max(result, dfs(str(a + b + c), n, ok))
                else:
                    result = min(result, dfs(str(a + b + c), n, ok))
        return result

print("{} {}".format(dfs(N, 0, False), dfs(N, 0, True)))
