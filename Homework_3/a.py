q = 100

def same(it):
    pass

def ver_mip(x):
    if randint(1,3)%2:#check consistent
        i = randint(0,q)
        return same(Ps[i,:](Q[i]))
    else:#check PCP
        P = zeros()
        R = zeros()
        Q = ver_pcp_queries(x)#|Q| = q
        for i in range(q):
            j = randint(0,q)
            R[i] = Ps[i,j](Q[i])
        return ver_pcp_check(R)
