# 연산자 끼워넣기 14888

maxValue = -1000000000
minValue = 1000000000

n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))


def minus(cur, number):
    if cur < 0:
        res = abs(cur) // number
        return -res
    else:
        return cur // number


def dfs(operator, cnt, cur):
    global maxValue, minValue
    if cnt == n:
        maxValue = max(maxValue, cur)
        minValue = min(minValue, cur)
        return
    else:
        for i in range(4):
            if operator[i] > 0:
                operator[i] -= 1
                if i == 0:
                    dfs(operator, cnt + 1, cur + numbers[cnt])
                elif i == 1:
                    dfs(operator, cnt + 1, cur - numbers[cnt])
                elif i == 2:
                    dfs(operator, cnt + 1, cur * numbers[cnt])
                elif i == 3:
                    dfs(operator, cnt + 1, minus(cur, numbers[cnt]))
                operator[i] += 1


dfs(operator, 1, numbers[0])

print(maxValue)
print(minValue)
