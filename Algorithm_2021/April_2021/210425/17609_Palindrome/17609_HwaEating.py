def pal(string,ans=0):
    n = len(string)
    rstring = string[::-1]
    for i in range(n):
        if string[i] != rstring[i]:
            if ans:
                return 2
            front = pal(string[:i]+string[i+1:],1)
            back = pal(string[:n-i-1] + string[n-i:],1)
            return min(front,back)
    return ans

for T in range(int(input())):
    string = input()
    print(pal(string))