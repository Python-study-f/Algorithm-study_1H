TC = int(input())

for tc in range(1, TC+1):
    문제왜이래 = input()
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    check = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    ret = ""
    tc_lst = list(input().split())

    print("#{0}".format(tc))

    for lst in tc_lst: # O(n) * O(1) = O(n)
        if lst in check:
            check[lst] += 1

    for key, value in check.items():
        print("{0}".format(key + ' ') * value, end= "")
    print()

