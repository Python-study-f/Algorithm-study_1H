s=input()
com=input()

#s=set(s)
cnt=0
i=0
while i<=len(s)-len(com):
    if s[i:i+len(com)]==com:
        cnt+=1
        i += len(com)
    else:
        i+=1
print(cnt)
