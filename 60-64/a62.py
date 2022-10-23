a = []
def fibon(n):
    if n== 0:
        a.append(0)
        return 0
    elif n ==1:
        a.append(1)
        return 1
    else:
        a.append(fibon(n-1))
        return fibon(n-1) + fibon(n-2)