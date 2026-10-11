desc = '1 +2 + 4 + 2^n-1 = (2^n)-1'
def Init():
    n = 4
    var = 0
    for i in range(1,n+1):
        var += 2**(i-1)

    print(var)
    print((2**n)-1)
