# 최대 상금 1244

T = int(input())


def dfs(cnt):
    global numbers, result
    if cnt == numtimes:
        result = max(int("".join(numbers)), result)
        return

    else:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                if ("".join(numbers), cnt) not in checkSet:
                    checkSet.add(("".join(numbers), cnt))
                    dfs(cnt + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]


for t in range(T):
    numbers, numtimes = input().split()
    numtimes = int(numtimes)
    numbers = list(numbers)
    result = 0
    checkSet = set()
    dfs(0)
    print(f"#{t + 1} {result}")

"""
    dfs 매개변수를 실수했다.
    dfs(num, cnt) 으로 놓고
    매번 호출때마다 num+1를 해주고 i값의 범위를 range(num, len(numbers)) 이렇게 놨는데
    이러니까 맨 왼쪽 numbers값을 비교안해주니 cnt값이 numbers 길이를 넘지 못했다.
    그래서 0이 나오는 현상이 발생됨. 이것만으로 2시간 넘게 고민한 것 같다. 아...
"""
