desc = "(3n-1) = n(1+3n)/2"
def Init():
    n = 2
    var = 0
    for i in range(1,n+1):
        var += (3*i)-1

    print(var)
    print((n*(1+3*n))//2)