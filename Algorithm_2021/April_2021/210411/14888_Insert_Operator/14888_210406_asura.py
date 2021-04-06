N = int(input())

data = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
# oper_cnt = list(map(int,input().split())
min_value, max_value = int(1e9), -int(1e9)

# operator = ['+'for _ in range(oper_cnt[0])] + ['-'for _ in range(oper_cnt[1])] + \
#            ['*'for _ in range(oper_cnt[2])] + ['/' for _ in range(oper_cnt[1])]
# 이 문제는 operator의 갯수만 dfs를 통해 계산하면 될 거 같아서 list로 만들지 않음


def dfs(i,ret,a,b,c,d):
    global min_value, max_value

    if i == len(data): # 연산자를 뺄 필요 그냥 count만 하면 되기 때문에 i라는 변수를 도입.
        max_value, min_value = max(ret, max_value), min(ret, min_value)
        return

    else:
        if a:
            dfs(i+1, ret+data[i],a-1,b,c,d)

        if b:
            dfs(i+1, ret-data[i],a,b-1,c,d)

        if c:
            dfs(i+1, ret*data[i],a,b,c-1,d)

        if d:
            dfs(i+1, int(ret/data[i]), a,b,c,d-1)

dfs(1,data[0],a,b,c,d)

print(max_value)
print(min_value)
'''
1. DFS 구현할 때 필요한 parameter 생각을 해보자
2. 문제 보자마자 DFS parameter들이 많을 것이라고 생각함. parameter에 넣을 값들을 고민했음.

3.입력을 리스트로 받아서 왜 왜 정답이 아닌지 한참 생각했음..
    생각해보니 dfs가 끝나면 값이 복구(?)되어야 하기 때문에 변수는 상관이 없지만 list는 뒤에 +1을 해줘야함
    개고생힘 ㅡㅡ..
    
def dfs(i,ret,oper):
        if oper[0]:
            oper[0] -= 1
            dfs(i+1, ret+data[i], oper)
            oper[0] += 1
'''


