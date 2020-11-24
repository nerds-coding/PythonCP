try:
    for _ in range(int(input())):
        s = input()

        ans = True
        for i in range(1,len(s)):
            if(s[i]!=s[i-1]):
                ans = False
                break
        if(ans):
            print(s)
        else:
            t = ''
            for _ in range(len(s)):
                t+='01'
            print(t)
        
except:
    pass