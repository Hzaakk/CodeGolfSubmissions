_,N,L,T=input().split()
x=len(N)
r=range
v=lambda J,n=0:n>=x and L[n-x]or str(eval(v(J,n*2+1)+'|&'[J[n]in'aA']+v(J,n*2+2)))
A=[[j for j in r(x)if i>>j&1and'Z'<N[j]]for i in r(2**x)if v(['oa'[(i>>j&('Z'<N[j]))-(N[j]in'aA')]for j in r(x)])==T]
print(*({str(i)[1:-1].replace(' ','')for i in A if len(i)==min(map(len,A))},*'SI')[bool(A)-(v(N)!=T)])
