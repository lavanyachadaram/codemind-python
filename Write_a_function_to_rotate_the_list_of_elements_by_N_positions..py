n=int(input())
d=list(map(int,input ().split()))
r=int(input())
r=r%n
if(r==0):
   print(*d)
else:
   print(*d[-r:]+d[:n-r])