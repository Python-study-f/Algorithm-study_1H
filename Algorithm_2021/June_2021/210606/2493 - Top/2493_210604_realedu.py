import sys 
r = sys.stdin.readline 

n = int(r()) 
t_list = list(map(int, r().split())) 

answer = [] 
stk = [] 

for i in range(n): 
  h = t_list[i] 
  if stk: 
    while stk: 
      if stk[-1][0] < h : 
        stk.pop() 
        if not stk: 
          print(0, end=' ') 
      elif stk[-1][0] > h: 
        print(stk[-1][1]+1, end=' ') 
        break 
      else : 
        print(stk[-1][1]+1, end=' ') 
        stk.pop() 
        break 
      stk.append([h, i])
  else: 
    print(0, end=' ') 
    stk.append([h,i])
