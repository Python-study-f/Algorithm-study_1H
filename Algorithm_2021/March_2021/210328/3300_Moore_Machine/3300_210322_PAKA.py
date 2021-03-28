import re

# main
for i in range(int(input())):
    inVal = input()
    inVal2 = input()

    # if go _
    patternA = "^" + re.sub("_", "[A-Z]+", inVal) +"$"
    # if don't go _
    patternB = "^" + re.sub("_", "", inVal) +"$"
    mA = re.match(patternA, inVal2)
    mB = re.match(patternB, inVal2)

    if not mA:
        print("!")
    elif mB:
        print("_")
    else:
        for i in range(26):
            c = chr(ord('A')+i)
            patternRST = "^" + re.sub("_", c, inVal) +"$"
            if re.match(patternRST, inVal2):
                print(c)