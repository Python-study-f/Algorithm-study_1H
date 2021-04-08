# def make_pw(idx=0,rule1=False,rule2=0,pick=[]):
#     if len(pick)==l and rule1 and rule2 >= 2:
#         ans.append(''.join(pick))
#         return
#     if idx == c:
#         return
#     if c - idx + len(pick) < l:
#         return
#     if pos[idx] in ['a','e','i','o','u']:
#         make_pw(idx+1, True, rule2, pick+[pos[idx]])
#     else:
#         make_pw(idx+1,rule1, rule2+1, pick+[pos[idx]])
#     make_pw(idx+1,rule1,rule2,pick)

# l,c = map(int,input().split())
# pos = input().split()
# pos.sort()
# ans = []
# make_pw()
# for i in ans:
#     print(i)

a = [[1,2,3]]*3
a[0][0] = 10
print(a)