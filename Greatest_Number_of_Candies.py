n=int(input())
l = list(map(int,input().split()))
k = int(input())
g = max(l)
for i in l:
  if(g<=(i+k)):
     print("True",end=" ")
  else:
    print("False",end=" ")