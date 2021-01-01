def solution(n, arr1, arr2):
    binary_list = []
    for i in range(n):
        binary = arr1[i] | arr2[i]
        binary2 = str(bin(binary)[2:])
        binary2 = binary2.zfill(n)
        binary_list.append(binary2.replace('1', '#').replace('0', ' '))
    return binary_list
