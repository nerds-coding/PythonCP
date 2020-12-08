def wordCount(dt,s,out = ''):
    if(not(s)):
        print(out)
        return
    
    for i in range(1,len(s)+1):
        pref = s[:i]
        if(pref in dt):
            wordCount(dt,s[i:],out+" "+pref)


dt = [
    "self", "th", "is", "famous", "Word",
    "break", "b", "r", "e", "a", "k", "br",
    "bre", "brea", "ak", "problem"
]

# input String
s = "Wordbreakproblem"

wordCount(dt, s)

