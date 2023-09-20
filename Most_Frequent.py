n=int(input())
k=list(map(int,input().split()))
a=0
s=set(k)
for i in s:
  c=k.count(i)
  if(c>a):
     a=c
     b=i
print(b)