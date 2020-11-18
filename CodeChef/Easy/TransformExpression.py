
for _ in range(int(input())):
    e = raw_input()
    stack = []
    rpn = ''

    pred = {'+':1,'-':1,'*':2,'/':2,'^':3}

    def isGreater(val):
        try:
            return True if(pred[val]<=stack[-1]) else False
        except(Exception)as e:
            return False
    
    for i in e:
        if(i.isalpha()):
            rpn+=i
        elif(i=='('):
            stack.append(i)
        elif(i==")"):
            while((not(stack==[])) and (stack[-1]!='(')):
                rpn+=stack.pop()
            if((not(stack==[]))and(stack[-1]!='(')):
                break
            else:
                stack.pop()
        else:
            while((not(stack==[]))and(isGreater(i))):
                rpn+=stack.pop()
            stack.append(i)
    while(not(stack==[])):
        rpn+=stack.pop()
    print(rpn)


