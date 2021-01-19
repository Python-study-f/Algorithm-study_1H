count = 0
while True:
    count += 1
    L, P, V = map(int, input().split()) 
    if L==0 and P==0 and V==0:
        break
    result = (V//P*L) + (V%P)
    print("Case" + str(count) + ":" + str(result))