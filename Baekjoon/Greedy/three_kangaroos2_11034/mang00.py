while True:
    try:
        one, two, three = map(int, input().split())
        movement_count = 0
        if (three - two) - 1 >= 1:
            movement_count = (three - two) - 1
        if (two - one) - 1 >= 1:
            if movement_count < (two - one) - 1:
                movement_count = (two - one) - 1
        print(movement_count)
    except EOFError:
        break
