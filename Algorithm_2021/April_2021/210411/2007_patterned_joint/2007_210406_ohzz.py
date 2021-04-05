# 패턴 마디의 길이 2007

T = int(input())
arr = []
for _ in range(T):
    arr.append(input())

for t in range(T):
    string = arr[t]
    for i in range(1, 11):
        tmp = string[0:i]
        if tmp == string[i : i * 2]:
            print(f"#{t + 1} {len(tmp)}")
            break
