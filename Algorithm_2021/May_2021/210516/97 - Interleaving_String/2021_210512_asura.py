class Solution(object):
    def isInterleave(self, s1, s2, s3):
        
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)

        if ls1 + ls2 != ls3:
            return False

        dp = [[False] * (ls2+1) for _ in range(ls1+1)]

        for i in range(len(s1)+1): # 가독성 좋게 그냥 len씀
            for j in range(len(s2)+1):
                if i == 0 and j == 0: # 0,0 은 True 값으로 설정
                    dp[i][j] = True
                elif i == 0: # 상한 표기
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]

                elif j == 0: # 하한 표기
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]