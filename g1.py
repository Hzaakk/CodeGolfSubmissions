I=eval(input().replace('][','],['))
R,C = len(I),len(I[0])
f=range
def t():
	for r in f(R):
		for c in f(C):
			y=i[r][c]
			x=y>>2
			l=i[r][c-1]if c!=0else-1
			d=i[r+1][c]if r!=R-1else-1
			if r==0and y&1or r==R-1and y&4or c==0and y&8or c==C-1and y&2or l!=-1and(x^l)&2!=0 or d!=-1and (x^d)&1!=0:
				return 0
	return 1
for x in f(4**(R*C)):
	i=I.copy()
	b=[]
	while x:
		b.insert(0,x%4)
		x//=4
	for j in f(len(b)):
		y,x=j//C,j%C
		n=i[y][x]
		i[y][x]=(n>>b[j])|(n<<4-b[j])&15
	if t():
		print(*i,sep='')
		break
else:
	print(-1)
