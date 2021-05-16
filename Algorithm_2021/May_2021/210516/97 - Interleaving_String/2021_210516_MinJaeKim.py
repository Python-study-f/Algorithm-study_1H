class Solution:
    def __init__(self):
        self.n=0
        self.m=0
        self.l=0
        self.s1=''
        self.s2=''
        self.s3=''
        self.ans=False

    def topdown(self, left, right): # topdown TLE
        if left==self.n-1 and right==self.m-1:
            self.ans=True
            return
        if left>self.n or right>self.m:
            return
        if left+right+2>=self.l:
            return
        if left+1<self.n and self.s3[left+right+2]==self.s1[left+1]:
            self.topdown(left+1, right)
        if right+1<self.m and self.s3[left+right+2]==self.s2[right+1]:
            self.topdown(left, right+1)


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.n= len(s1)
        self.m= len(s2)
        self.l=len(s3)
        if self.n+self.m!=self.l:
            return False
        if not s1 and not s2 and not s3:
            return True
        self.dp=[[False]*(self.m+1) for _ in range(self.n+1)]
        self.dp[0][0]=True
        for left in range(-1,self.n): # bottomup AC
            for right in range(-1,self.m):
                if self.dp[left+1][right+1] and left+1<self.n and self.s3[left+right+2]==self.s1[left+1]:
                    self.dp[left+2][right+1]=True
                if self.dp[left+1][right+1] and right+1<self.m and self.s3[left+right+2]==self.s2[right+1]:
                    self.dp[left+1][right+2]=True
                    
        #[print(*el) for el in self.dp]

        # return self.topdown(-1,-1) TLE
        return self.dp[self.n][self.m]