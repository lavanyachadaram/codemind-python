n=int(input())
s=list(map(int,input().split()))
k=s.copy()
k.sort()
for i in range(len(k)):
  print(k.index(s[i]),end=" ")