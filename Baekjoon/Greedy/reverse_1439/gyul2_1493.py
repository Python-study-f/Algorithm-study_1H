S= input()
cnt = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt = cnt +1
    result = (cnt+1) //2
print(result)