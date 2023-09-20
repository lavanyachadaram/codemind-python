n=int(input())
k=list(map(int,input().split()))
for i in range(n):
  b=k[i]
  if(k.count(b)>n//2):
     print(b)
     break