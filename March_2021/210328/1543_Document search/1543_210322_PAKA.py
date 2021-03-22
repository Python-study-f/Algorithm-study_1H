inVal1 = input()
inVal2 = input()
rst = 0

n = inVal1.find(inVal2)
while n != -1:
    # add padding _
    inVal1 = inVal1[0:n] + "_" + inVal1[n+len(inVal2):]
    n = inVal1.find(inVal2)
    rst += 1

print(rst)