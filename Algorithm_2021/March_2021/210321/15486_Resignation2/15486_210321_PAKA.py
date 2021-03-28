n = int(input())
# 마지막날 하루짜리 상담을 위해 + 1
gain = [0] * (n + 1)
tT = [0] * n
pT = [0] * n

#init
for i in range(n):
  t, p = map(int, input().split())
  tT[i] = t
  pT[i] = p

# n-1 ~ 0까지 반복
for i in range(n-1, -1, -1):
  canWork = i + tT[i]
  if n < canWork:
    gain[i] = gain[i+1]
  else:
    gain[i] = max(gain[i+1], gain[canWork] + pT[i])
    #print(gain[i+1], gain[canWork], pT[i], i)
  #print(gain)
  
print(gain[0])