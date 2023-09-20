s=0
a=int(input())
b=int(input())
for i in range(a):
   k=list(map(int,input().split()))
   s+=sum(k)
print(s)