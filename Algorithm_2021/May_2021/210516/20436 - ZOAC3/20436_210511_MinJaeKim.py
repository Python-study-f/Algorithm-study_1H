#dic={'q': True, 'w': True, 'e': True, 'r': True, 't': True, 'a': True, 's': True, 'd': True, 'f': True, 'g': True, 'z': True, 'x': True, 'c': True, 'v': True}
keyboard=[]
keyboard.append([('q',0),('w',0),('e',0),('r',0),('t',0),('y',1),('u',1),('i',1),('o',1),('p',1)])
keyboard.append([('a',0),('s',0),('d',0),('f',0),('g',0),('h',1),('j',1),('k',1),('l',1)])
keyboard.append([('z',0),('x',0),('c',0),('v',0),('b',1),('n',1),('m',1)])
a, b= input().split()
left, right=0,0
for i in range(3):
    for j in range(len(keyboard[i])):
        if keyboard[i][j][0]==a:
            left= [i,j]
        if keyboard[i][j][0]==b:
            right=[i,j]

s= input()
ans=0
for el in s:
    flag=False
    for i in range(3):
        for j in range(len(keyboard[i])):
            if keyboard[i][j][0]==el:
                flag=True
                if keyboard[i][j][1]==0:
                    ans+=abs(left[0]-i)+abs(left[1]-j)
                    left=[i,j]
                else:
                    ans+=abs(right[0]-i)+abs(right[1]-j)
                    right=[i,j]
                break
                
        if flag:
            break
print(ans+len(s))
