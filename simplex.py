m=int(input("if it is minimum press 0 or else press 1"))
n=int(input("enter no of variables present in objective function"))
x=[]
for i in range(n):
    if m==0:
        k=(int(input("enter coefficients of x")))
        x.append(k-2*k)
    else:
        x.append(int(input("enter coefficients of x")))
k=int(input("enter no of constraints present"))
con=[]
for i in range(n):
    for j in range(k):
        con.append(int(input("enter coefficients of x in constraints")))
constant=[]
for i in range(k):
    constant.append(int(input("enter constants of constraints")))
def conversion(con):
    res=[]
    
    i=0
    for j in range(k):
        res.append(con[i:i+n])
        i=i+n
    return res
cs=[]
cs=conversion(con)
cb=[]
for i in range(k):
    cb.append(0)
s=[]
for i in range(k):
    for j in range(k):
        if(i==j):
            s.append(1)
        else:
            s.append(0)
slack=[]
i=0
for j in range(k):
    slack.append(s[i:i+k])
    i=i+k
for i in range(k):
    x.append(0)
xi=cs[:]
for i in range(k):
    xi[i].extend(slack[i])
def zjvalues(cb,xi):
    zj=[]
    
    for i in range(n+k):
        p=0
        for j in range(k):
            p=p+cb[j]*xi[j][i]
        zj.append(p)
    return zj
while True:
    zj=zjvalues(cb,xi)
    deltaj=[]
    for i in range(n+k):
        deltaj.append(zj[i]-x[i])
    p=0
    for i in range(n+k):
        if (deltaj[i]>=0):
            p=p+1
    if(p==n+k):
        break
            
    mi=min(deltaj)
    def minindex(deltaj,m):
        for i in range(n+k):
            if(deltaj[i]==m):
                return i
    cindex=minindex(deltaj,mi)
    minratio=[]
    for i in range(k):
        try:
            minratio.append(constant[i]/xi[i][cindex])
        except ZeroDivisionError:
            minratio.append(10000)
        except:
            pass
    mimi=min(minratio)
    sameindex=[]
    p=0
    for j in range(2,k+2):
        for i in range(k):
            if (mimi==minratio[i]):
                sameindex.append(i)
                p=p+1
        if(p!=1):
            print("it is degenerate model")
            minratio.clear()
            for i in range(len(sameindex)):
                minratio.append(xi[sameindex[i]][j]/xi[sameindex[i]][cindex])
            mimi=min(minratio)
            sameindex.clear() 
            p=0
        else:
            break
    rindex=minindex(minratio,mimi)
    cb[rindex]=x[cindex]
    keyelement=xi[rindex][cindex]
    constant[rindex]=constant[rindex]/keyelement
    for i in range(n+k):
        xi[rindex][i]=xi[rindex][i]/keyelement
    nonkey=[]
    for i in range(k):
        if(rindex==i):
            for j in range(k):
                if (j!=i):
                    nonkey.append(j)
    for i in range(0,len(nonkey)):
        constant[nonkey[i]]=constant[nonkey[i]]-xi[nonkey[i]][cindex]*constant[rindex]
    for i in range(len(nonkey)):
        p=xi[nonkey[i]][cindex]
        for j in range(n+k):
            xi[nonkey[i]][j]=xi[nonkey[i]][j]-p*xi[rindex][j]
z=0
for i in range(k):
    z=z+cb[i]*constant[i]
print("the optimum solution of z is {}".format(z))
