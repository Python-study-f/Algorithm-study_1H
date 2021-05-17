def solution(stones, k):
    answer = 0
    dp = [0]*len(stones)
    for i in range(k):
        dp[i] = stones[i]
        
    for i in range(k, len(stones)):
        dp[i] = 0
        for j in range(1, k+1):
            dp[i] = max(dp[i], dp[i-j])
        if stones[i] < dp[i]:
            dp[i] = stones[i]
        
    for i in range(1, k+1):
        answer = max(answer, dp[len(stones)-i])
    return answer
  
 # 정확성 100.0 효율성 0.0 점 코드 => 총 64.1
 # 이진탐색을 적용해서 다시 풀어 볼 예정
