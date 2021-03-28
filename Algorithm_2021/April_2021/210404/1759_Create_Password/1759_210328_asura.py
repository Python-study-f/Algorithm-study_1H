from itertools import combinations

N, M = map(int,input().split())
data = list(map(str,input().split()))

lst = list(combinations(data,N))
vowel = "aeiou"

st = []

for i in lst:
    vow_cnt = 0
    not_vow = 0

    for j in i:
        if j in vowel:
            vow_cnt += 1
        else:
            not_vow += 1

    if vow_cnt == 0 or not_vow<2:
        continue

    i = sorted(i)
    i = ''.join(i)
    st.append(i)


st = sorted(list(set(st)))

for i in range(len(st)):
    print(st[i])

