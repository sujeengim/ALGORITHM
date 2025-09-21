while True:
    l = list(input())
    if (l[0] == "."):
        break
    new_l = list(filter(lambda x: (x in "[]()"), l))

    stack = []

    for i in new_l:
        if (i == "("):
            stack.append(i)
        elif (i == "["):
            stack.append(i)
        elif (i==")"):
            if (len(stack) == 0 or stack[-1] != "("):
                print("no")
                break
            else:
                stack.pop()
        elif (i=="]"):
            if (len(stack) == 0 or stack[-1] != "["):
                print("no")
                break
            else:
                stack.pop()
    else:
        print("yes" if (len(stack) == 0) else "no")