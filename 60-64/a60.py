def recur(n):
    if(n == 0):
        return 0
    return recur(n-1) + 100


recur(5)