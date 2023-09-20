n=int(input())
k=list(map(int,input().split()))
for i in range(n):
   c=k[i]
   if(k.count(c)>1):
      print(c)
      break