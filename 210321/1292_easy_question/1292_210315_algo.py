a,b=map(int,input().split())

temp=[]
sum=0
for i in range(1,1001):
    for j in range(1,i+1):
        temp.append(i)
for i in range(a-1,b):
    #print(temp[i])
    sum+=temp[i]

print(sum)
