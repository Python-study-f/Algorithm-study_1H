while True:
    try:
        a, b, c = map(int, input().split())
        num_list = []
        num_list.append(b - a)
        num_list.append(c - b)
        answer = max(num_list) - 1
        print(answer)
    except EOFError:
        break
