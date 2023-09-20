n=int(input())
c=0
e=0
k=list(map(int,input().split()))
for i in range(n):
  if(k[i]%2==0):
      e+=1
  else:
    c+=1
print(e,c)    