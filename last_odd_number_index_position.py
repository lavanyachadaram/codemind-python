n=int(input())
I=list(map(int,input().split()))
for i in range(n):
  if(I[i]%2==1):s=i
print(s)  