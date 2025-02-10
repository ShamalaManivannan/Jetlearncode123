open_list = ['[','{','(']
closed_list = ['[','{','(']
def check(mystr):
    stack = []
    for i in mystr:
        if i in open_list:
            stack.append(i)
        elif i in closed_list:
            pos = closed_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[-1])):
                stack.pop()
            else:
                return "unbalanced"  
    if len(stack) == 0:
        return "balanced"    
    else:
        return "unbalanced"  

string = "{"      
print(string,"-",check(string))

