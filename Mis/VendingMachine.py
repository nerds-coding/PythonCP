ty = ['TY01', 'TY02', 'TY04', 'TY03']
sy = ['SY01', 'SY03', 'SY02', 'SY04', 'SY05']

ty = sorted(ty, key=lambda x: x.split('0'))
sy = sorted(sy)
# syc = sy.split(0)
tyc = [x.split('0')[1] for x in ty]
syc = [x.split('0')[1] for x in sy]
mx = max(len(ty), len(sy))

for i in range(1, mx+1):
    try:
        if(str(i) in tyc):
            print(ty[i-1], end='')

        else:
            print('Absent', end='')
    except(Exception)as e:
        pass
    try:
        if(str(i) in syc):
            print(sy[i-1], end='')

        else:
            print('Absent', end='')
    except(Exception)as e:
        pass
    print()
