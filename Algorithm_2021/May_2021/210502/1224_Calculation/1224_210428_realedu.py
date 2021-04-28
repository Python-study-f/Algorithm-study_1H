

icp = {'*':2, '+':1, '(':3} # coming
isp = {'*':2, '+':1, '(':0} # stack

for t in range(1, 11):
    N = int(input())
    t_case = input()
    result = []
    operator = []

    # 중위 연산 -> 후위 연산
    for i in range(N):
        if t_case[i].isdigit(): # 숫자 판별
            result.append(t_case[i])

        else: # 연산자
            if not operator: # 연산자 리스트에 연산자 없으면 추가
                operator.append(t_case[i])
                continue

            # 여는 괄호가 나올 때 까지 pop
            if t_case[i] == ')':
                while operator[-1] != '(':
                    result.append(operator.pop())
                operator.pop()  # ( 최종적으로 pop

            # ex : (*, + ||||| '(') ('(' ||||| *, +)
            elif icp[t_case[i]] > isp[operator[-1]]:
                operator.append(t_case[i])

            else:
                # icp가 isp보다 작으면 icp > isp될 때 까지 계속 pop
                # ex : icp : +, isp : *
                while icp[t_case[i]] <= isp[operator[-1]]:
                    result.append(operator.pop())
                operator.append(t_case[i])  # 마지막에 연산자 리스트에 추가

    # 계산 처리
    stack = []

    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            if i == '+':
                stack.append(n1 + n2)
            elif i == '*':
                stack.append(n1 * n2)
    
        # print(stack)
    # print()

    print('#{} {}'.format(t, stack[0]))

