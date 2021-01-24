n= int(input())

count_coin= 0

#거슬러 줄 수 없는 경우
if n in [1,3]:
    count_coin = -1
elif (n%5)%2 == 0:
    count_coin = n//5 + (n%5)//2
else:
    count_coin = ((n//5)-1) + (n%5+5)//2
print(count_coin)