def bracket_checker(brackets):
    stack=[]
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        if bracket == "[" :
            stack.append(bracket)
        if bracket == "{":
            stack.append(bracket)
    for bracket in "}])":
        if bracket == ")" and stack[-1] == "(":
            stack.pop()
        elif bracket == "]" and stack[-1] == "[":
            stack.pop()
        elif bracket == "}" and stack[-1] == "{":
            stack.pop()
        else:
             return False
    return True


n =(bracket_checker("([{}])"))
print(n)
