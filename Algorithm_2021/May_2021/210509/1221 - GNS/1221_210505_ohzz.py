# GNS 1221 SW Expert

T = int(input())

comp = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9,
}

comp2 = {
    0: "ZRO",
    1: "ONE",
    2: "TWO",
    3: "THR",
    4: "FOR",
    5: "FIV",
    6: "SIX",
    7: "SVN",
    8: "EGT",
    9: "NIN",
}


for _ in range(T):
    t, length = input().split()
    length = int(length)
    arr = list(input().split())
    print(t)
    for i in range(length):
        arr[i] = comp[arr[i]]
    arr.sort()
    for i in range(length):
        print(comp2[arr[i]], end=" ")
    print()
