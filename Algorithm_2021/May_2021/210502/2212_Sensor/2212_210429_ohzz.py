# 센서 2212 백준

n = int(input())
k = int(input())

arr = list(map(int, input().split()))

arr.sort()

diff = []
for i in range(1, n):
    diff.append(arr[i] - arr[i - 1])

diff.sort(reverse=True)

print(sum(diff[k - 1 :]))

# k개 만큼의 집중국이 있어야하는데 이 말이 이해 안됐음. 그런데 그냥 k개의 구간이라고 생각하니까 이해가 됨

# 1 6 9 3 6 7 센서
# 1 3 6 6 7 9 센서 정렬
# 2 3 0 1 2 센서 간에 길이 차이

# k -    1  |  2
#       1 3 | 6 6 7 9
#        2  | 0 + 1 + 2 = 3
#           합 : 5
# 가장 큰 센서간에 길이 차이를 k-1개 없애주고 더하면 값이 나옴
