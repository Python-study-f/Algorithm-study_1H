# LIS : Longest Increasing Subsequence 최장 증가 부분 수열 문제
# https://mygumi.tistory.com/69
# https://mygumi.tistory.com/142
# 두 링크 공부하시면 좋을 거 같습니다! 진짜 잘 설명되어있음요
# 본 풀이는 O(n^2)

#-- 입력 --#
N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

#-- 세팅 --#
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if data[i] > data[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(N - max(dp))

'''
i j

Ao = [10,20,10,30,20,50]
dp = [ 1, 2, 1, 3, 1, 1]
'''
