desc = "(1+1/n) = n+1"
def Init():
    n = 2
    var = 0
    for i in range(1,n+1):
        var += 1+(1//i)

    print(var)
    print(n+1)