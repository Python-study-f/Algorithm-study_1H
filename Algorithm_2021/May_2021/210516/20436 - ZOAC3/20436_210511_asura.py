left, right = map(str,input().split())
data = list(input())
ans = 0
# Key, x,y 좌표
left_list = { "z":(1,1),"x":(1,2),"c":(1,3),"v":(1,4),"a":(2,1),"s":(2,2),"d":(2,3),"f":(2,4),"g":(2,5),
             "q":(3,1),"w":(3,2),"e":(3,3),"r":(3,4),"t":(3,5) }

right_list = { "b":(1,5),"n":(1,6),"m":(1,7),"h":(2,6),"j":(2,7),"k":(2,8),"l":(2,9),"y":(3,6),"u":(3,7),
              "i":(3,8),"o":(3,9),"p":(3,10) }


for ch in data:
    a,b = left_list[left]
    c,d = right_list[right]


    if ch in left_list:
        x,y = left_list[ch]
        ans += 1 + abs(x-a) + abs(y-b)
        left = ch

    elif ch in right_list:
        x,y = right_list[ch]
        ans += 1 + abs(x-c) + abs(y-d)
        right = ch


print(ans)