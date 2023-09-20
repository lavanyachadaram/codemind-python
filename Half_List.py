n=int(input())
k=list(map(int,input().split()))
for i in range(n-1,n//2-1,-1):
   print(k[i],end=" ")
for j in range(n//2):
   print(k[j],end=" ")