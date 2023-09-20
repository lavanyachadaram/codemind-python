def square(a):
  t=a
  x=True
  for i in range(1,a+1):
     if(i*i==t):
        x=True
        break
     else:
        x=False
  return x
n=int(input())
k=list(map(int,input().split()))
c=0
for j in range(n):
  b=k[j]
  if(square(b)==True):
     c+=k[j]
print(c)      
      
