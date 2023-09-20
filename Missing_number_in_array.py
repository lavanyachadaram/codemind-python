n=int(input())
for i in range(1,n+1):
  q=int(input())
  k=list(map(int,input().split()))
  l=1
  while True:
    if l not in k:
        print(l)
        break
    l+=1