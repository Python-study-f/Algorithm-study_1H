import sys; input= lambda: sys.stdin.readline().rstrip()
s= input()
ths=input()
n= len(s)
m=len(ths)

cur=0
stc=[]
stk=0
def chk():
    flag=True
    for i in range(-1, -1-m,-1):
        if ths[i]!=stc[i]:
            flag=False
            break
    if flag:
        for _ in range(m):
            stc.pop()
        return True
    return False

for i in range(n):
    stc.append(s[i])
    stk+=1
    if s[i]==ths[m-1] and stk>=m:
        if chk():
            stk-=m
ans=''.join(stc)
print([ans,'FRULA'][not ans])