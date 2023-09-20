n=int(input())
k=list(map(int,input().split()))
a=0
for i in range(n):
  b=k[i]
  l=len(str(b))
  if(l%2==0):
     a+=1
print(a)