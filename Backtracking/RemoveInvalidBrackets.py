def removeInvalid(s):
    all = list()
    temp = list(s)
    new = ''
    for i in range(len(temp)):
        del temp[i]
        for j in temp:
            if(j == '('):
                new+=j
                all.append(j)
            if(j==')')and(all!=[]):
                new+=j
                all.pop()
        if(all==[]):
            print(new)
        temp = list(s)
        new= ''

removeInvalid('()())()')