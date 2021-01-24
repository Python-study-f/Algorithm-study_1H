#틀렸습니다!

#input style :  2 3 5  
#input-> split 처리해서 리스트에 넣어야함

kangaroo = list(map(int, input().split())) #한줄위에 있으니까 리스트로 처리
count = 0


while True:
    distance1 = abs(kangaroo[0] - kangaroo[1])  #절대값으로 계산
    distance2 = abs(kangaroo[1] - kangaroo[2]) #절대값으로 계산 
    #break 조건
    if distance1 == 1 and distance2 ==1:
        break
    #뛰어보자 캥거루들
    if distance1 < distance2: #뒤에서 앞으로 뛰어야함
        kangaroo.pop(0)
        kangaroo.insert(1, kangaroo[-1]-1) #뒤에서 한칸 앞으로
    else: # 앞에서 뒤로 뛰어야함
        kangaroo.pop()
        kangaroo.insert(1, kangaroo[0]+1)
    count = count + 1
print(count)