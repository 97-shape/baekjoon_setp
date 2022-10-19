while True:
    s = input()
    if s == ".":
        break

    stack = []
    flag = True
    for x in s:
        if x == "(" or x == "[":
           stack.append(x) 
        elif x == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif x == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    
    if flag and not stack:
        print("yes")
    else:
        print("no")