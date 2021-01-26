while True: 
#    try:
#        kangaroo = list(map(int, input().split())) 
#        kangaroo = kangaroo.sort
#        success=[]
#        #typeerror 발생 
#        # 'builtin_function_or_method' object is not subscriptable
#        distance1 = kangaroo[1] - kangaroo[0]  
#        distance2 = kangaroo[2] - kangaroo[1] 
#        success.append(distance1)
#        success.append(distance2)
#        count = max(success)-1
#        print(count)
 
    try:
        kang1, kang2, kang3 = list(map(int, input().split())) 
        success=[]
        distance1 = kang2-kang1
        distance2 = kang3-kang2 
        success.append(distance1)
        success.append(distance2)
        count = max(success)-1
           
        
        print(count)
        
    except EOFError:
        break