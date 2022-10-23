def fibon(n):
    if n== 0:
        return 0
    elif n ==1:
        return 1
    else: return fibon(n-1) + fibon(n-2)