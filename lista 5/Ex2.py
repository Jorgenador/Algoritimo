desc = "somatorio até n onde i=1 em etapas de i(i+1) = (n(n+1)(n+2))/3"
def Init():
    n = 6
    var = 0
    for i in range(1,n+1):
        var += i*(i+1)

    print(var)
    print((n*(n+1)*(n+2))//3)