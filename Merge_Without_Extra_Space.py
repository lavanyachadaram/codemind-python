n=int(input())
for i in range(n):
  a,b=map(int,input().split())
  k=list(map(int,input().split()))
  r=list(map(int,input().split()))
  k.extend(r)
  k.sort()
  print(*k)