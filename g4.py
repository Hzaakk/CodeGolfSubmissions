n,r,I='5 -90 ┌┐.┌┐│├┬┤││├┼┤││├┴┤│╘┘.└┘'.split()
m=*[-9425]*4,*map(ord,'		\n\n\r-%51&9/(6 .\'7!0)8"3+:#2*;$4,<====>A?B@C@CDEGFHKIJLLLLMOMONPNPQRQRSW\ZTV]YUX^[_fbi`echagdjklklmmmmnopqrsrsttttuvwxyz{|}~')
n=int(n)
r=int(r)//90%4
for i in range(len(I)):exec('i=(n-i%n-1)*n+i//n;'*r);a=m.index(ord(I[i])-9471);print(chr(m[a-a%4+(a+r)%4]+9471),end='')    
