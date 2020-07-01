I=eval(input().replace('][','],['))
s=len
f=range
R,C=s(I),s(I[0])
Q=C+1
p=P=[[0]*C]
I=[[0,*e,0] for e in P+I+P]
b=0
for a in f(4**(R*C)):
	i,j=[m[:]for m in I],0
	while a:
		n=i[j//C+1][j%C+1]
		i[j//C+1][j%C+1],a,j=n>>a%4|n<<4-a%4&15,a//4,j+1
	for r in f(Q*R+Q):
		r,c=r//Q,r%Q+1
		y=i[r][c]
		if(y>>2^i[r][c-1])&2|(y>>2^i[r+1][c])&1:break
	else:b,p=1,i
print((-1,'['+''.join(str(j[1:-1]).replace(' ','')for j in p[1:-1])+']')[b])
